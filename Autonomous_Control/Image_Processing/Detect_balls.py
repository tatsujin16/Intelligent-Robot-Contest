#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ColorExtract(object):
	def __init__(self):
		self._blue_pub = rospy.Publisher('blue_image', Image, queue_size=1)
		self._red_pub = rospy.Publisher('red_image', Image, queue_size=1)
		self._yellow_pub = rospy.Publisher('yellow_image', Image, queue_size=1)
		self._cv_image_pub = rospy.Publisher('cv_image', Image, queue_size=1)

		self._image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
		self._bridge = CvBridge()

	def get_colored_area(self, cv_image, lower, upper):
		hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
		mask_image = cv2.inRange(hsv_image, lower, upper)
		area = cv2.countNonZero(mask_image)
		return (area, mask_image)
	
	def Noise_processing(self, img_color):
		kernel = np.ones((10,10),np.uint8)
		gray = cv2.GaussianBlur(img_color,(33,33),1)
		gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE,kernel)
		gray = cv2.GaussianBlur(img_color,(33,33),1)
		return gray 

	def callback(self, data):
		try:
			cv_image = self._bridge.imgmsg_to_cv2(data, 'bgr8')
		except CvBridgeError, e:	
			print e

		blue_area, blue_image1 = self.get_colored_area(cv_image, np.array([100,108,17]), np.array([150,255,255]))
		yellow_area, yellow_image1 = self.get_colored_area(cv_image, np.array([20,96,66]), np.array([40,255,255]))
		red_area1, red_image1 = self.get_colored_area(cv_image, np.array([170,114,56]), np.array([180,255,255]))
		red_area2, red_image2 = self.get_colored_area(cv_image, np.array([0,114,56]), np.array([10,255,255]))
		red_area = red_area1 + red_area2
		red_image3 = red_image1 + red_image2
		blue_image = self.Noise_processing(blue_image1)
		yellow_image = self.Noise_processing(yellow_image1)
		red_image = self.Noise_processing(red_image3)
		
		try:
			self._blue_pub.publish(self._bridge.cv2_to_imgmsg(blue_image, 'mono8'))			
			self._red_pub.publish(self._bridge.cv2_to_imgmsg(red_image, 'mono8'))			
			self._yellow_pub.publish(self._bridge.cv2_to_imgmsg(yellow_image, 'mono8'))		
			self._cv_image_pub.publish(self._bridge.cv2_to_imgmsg(cv_image, 'bgr8'))	
		except CvBridgeError, e:
			print e
		rospy.loginfo('blue=%d, red=%d, yellow=%d' % (blue_area, red_area, yellow_area))
	
if __name__ == '__main__':
	rospy.init_node('color_extract')
	color = ColorExtract()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
