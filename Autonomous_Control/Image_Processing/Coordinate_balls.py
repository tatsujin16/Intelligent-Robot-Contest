#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
import math
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist

class first(object):
	def __init__(self):
#sub
		self._sub_tag0 = rospy.Subscriber('/tag0_info', Twist, self.callback_tag0)
		self._sub_tag1 = rospy.Subscriber('/tag1_info', Twist, self.callback_tag1)
		self._cv_image_sub = rospy.Subscriber('cv_image', Image, self.callback, 'img')
		self._blue_sub = rospy.Subscriber('blue_image', Image, self.callback, 'blue')
		self._red_sub = rospy.Subscriber('red_image',Image,  self.callback, 'red')
		self._yellow_sub = rospy.Subscriber('yellow_image', Image, self.callback,'yellow')
		self._bridge = CvBridge()
#pub		
		self._cv_image2_pub = rospy.Publisher('cv_image2', Image, queue_size=1)
		self._pub_redxy = rospy.Publisher('/red_xy', Twist, queue_size=1)
		self._pub_bluexy = rospy.Publisher('/blue_xy', Twist, queue_size=1)
		self._pub_yellowxy = rospy.Publisher('/yellow_xy', Twist, queue_size=1)

		self._cam_posi = np.zeros(3, dtype = 'float64')
		self._angle_r = np.zeros(3, dtype = 'float64')
		self._local_tag1 = np.zeros(3, dtype = 'float64')	
		self._tag1_angle_r = np.zeros(3, dtype = 'float64')
		self._vacuum_posi = np.zeros(1, dtype= 'float64')

	def callback_tag0(self, message):
		self._cam_posi[0] = message.linear.x
		self._cam_posi[1] = message.linear.y
		self._cam_posi[2] = message.linear.z
		self._angle_r[0] = message.angular.x
		self._angle_r[2] = message.angular.z

	def callback_tag1(self, message1):
		self._local_tag1[0] = message1.linear.x
		self._local_tag1[1] = message1.linear.y 
		self._local_tag1[2] = message1.linear.z
		self._tag1_angle_r[2] = message1.angular.z
		self._vacuum_posi[0] = self._local_tag1[1] - 0.35
		
	def callback(self, data, name):
		global flag, FLAG, cv_image1, Mask_color
		if(name == 'img'):
			cv_image1 = self._bridge.imgmsg_to_cv2(data, 'bgr8')
			flag = 1
		elif(name == 'red' or name == 'blue' or name == 'yellow'):
			Mask_color = self._bridge.imgmsg_to_cv2(data, 'mono8')
			FLAG = 1
		if(flag == 1 and FLAG == 1):
			cv_image2 = self.get_Contours(Mask_color, cv_image1, name)
			self._cv_image2_pub.publish(self._bridge.cv2_to_imgmsg(cv_image2, 'bgr8')) 

	def _Squaring(self, x, y):
		Shaded = np.sqrt(x*x + y*y)
		return Shaded

	def get_Contours(self, mask_color, cv_image, color):
		global count
		count = 0
		imaEdge, contours, hierarchy = cv2.findContours(mask_color,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		if(len(contours) == 0):
			if(color == 'red'):
					red_xy = Twist()
					red_xy.linear.x = 0
					red_xy.linear.y = 0
					self._pub_redxy.publish(red_xy)
					print "4"
			elif(color == 'blue'):
					blue_xy = Twist()
					blue_xy.linear.x = 0
					blue_xy.linear.y = 0
					self._pub_bluexy.publish(blue_xy)
					print "5"
			elif(color == 'yellow'):
					yellow_xy = Twist()
					yellow_xy.linear.x = 0
					yellow_xy.linear.y = 0
					self._pub_yellowxy.publish(yellow_xy)
					print "6"
		for kazu in range(len(contours)):
			cnt = contours[kazu]
			circularity, AREA, Radius = self.Circul_Level(cnt)
			Radius = int(Radius)
			if(circularity >= 0.80 and AREA >= 200):
				x,y,w,h = cv2.boundingRect(cnt)
				kari_center_x = x + Radius
				kari_center_y = y + Radius
				center_x = (kari_center_x - (cv_image.shape[1]/2))
				center_y = (kari_center_y - (cv_image.shape[0]/2))*(-1)
				cv_image = cv2.rectangle(cv_image,(x,y),(x+w,y+h), (0,255,0),2)
				cv_image = cv2.circle(cv_image,(kari_center_x,kari_center_y),2,(0,255,0),-1) 
				a,b = self.Position_estimation(center_x, center_y)
				AA,BB = self.Transform(a,b)
				if(color == 'red'):
#					print "red[%d] = (%lf,%lf)" %(kazu+1, AA, BB)
					vacuum_dis = self._Squaring(AA, BB) 
					red_xy = Twist()
					red_xy.linear.x = round(AA,2)
					red_xy.linear.y = round(BB,2)
					red_xy.angular.z = round(vacuum_dis,2)
					self._pub_redxy.publish(red_xy)
					count = count + 1
				elif(color == 'blue'):
#					print "blue[%d] = (%lf,%lf)" %(kazu+1, AA, BB)
					vacuum_dis = self._Squaring(AA, BB) 
					blue_xy = Twist()
					blue_xy.linear.x = round(AA,2)
					blue_xy.linear.y = round(BB,2)
					blue_xy.angular.z = round(vacuum_dis,2)
					self._pub_bluexy.publish(blue_xy) 
					count = count + 1
				elif(color == 'yellow'):
#					print "yellow[%d] = (%lf,%lf)" %(kazu+1, AA, BB)
					vacuum_dis = self._Squaring(AA, BB) 
					yellow_xy = Twist()
					yellow_xy.linear.x = round(AA,2)
					yellow_xy.linear.y = round(BB,2)
					yellow_xy.angular.z = round(vacuum_dis,2)
					self._pub_yellowxy.publish(yellow_xy)
					count = count + 1

		print "count = %d" %(count)
			
		if(count == 0 and color == 'red'):
			red_xy = Twist()
			red_xy.linear.x = 0
			red_xy.linear.y = 0
			self._pub_redxy.publish(red_xy)
		if(count == 0 and color == 'blue'):
			blue_xy = Twist()
			blue_xy.linear.x = 0
			blue_xy.linear.y = 0
			self._pub_bluexy.publish(blue_xy)
		if(count == 0  and color == 'yellow'):
			yellow_xy = Twist()
			yellow_xy.linear.x = 0
			yellow_xy.linear.y = 0
			self._pub_yellowxy.publish(yellow_xy)
			
		return cv_image

	def Circul_Level(self, CNT):
		area = cv2.contourArea(CNT)
		length = cv2.arcLength(CNT, True)
		Circularity = 4.0*np.pi*area/(length*length)
		radius = np.sqrt(area/np.pi)
		if(radius<0):
			radius*(-1)
		return Circularity, area, radius

	def Position_estimation(self, C_X, C_Y):
		fy = 968.412572
		h = self._cam_posi[2] + 0.041 
		shita = self._angle_r[0]
		C_X1 = abs(C_X)
		C_Y1 = abs(C_Y)
		delta_shita = math.atan2(C_Y1, fy)
		if(C_Y <= 0.0):
			a = shita + delta_shita
		elif(C_Y > 0.0):
			a = shita - delta_shita
		yt =  h  / np.tan(a)
		f_dash = np.sqrt(fy*fy + C_Y1*C_Y1)
		xt = (C_X1*np.sqrt(yt*yt + h*h)) / f_dash
		if(C_X < 0.0):
			xt = xt*(-1)
		return xt, yt

#回転行列
	def make_rot_mat(self, angle, c_x, c_y):
		rot_matrix = [[np.cos(angle),np.sin(angle),c_x],[(-1)*np.sin(angle),np.cos(angle),c_y]]
		rot_matrix = np.matrix(rot_matrix)
		return rot_matrix

	def Transform(self, ball_x, ball_y): 
		angle = (-1)*(self._tag1_angle_r[2])
		c_x = self._local_tag1[0]
		c_y = self._vacuum_posi[0]
		from_camera_to_ball =  np.array([ball_x, ball_y,1])
		rot_mat = self.make_rot_mat(angle, c_x, c_y)
		rot_xy = np.dot(rot_mat, from_camera_to_ball.reshape(3,1))
		para_rot_x, para_rot_y = rot_xy[0, 0], rot_xy[1, 0]		
		return para_rot_x ,para_rot_y

if __name__ == '__main__':
	rospy.init_node('senbetu')
	first = first()
	try:
		flag = 0
		FLAG = 0
		count = 0
		rospy.spin()
	except KeyboardInterrupt:
		pass
