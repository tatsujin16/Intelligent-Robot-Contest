#!/usr/bin/env python

import rospy
import numpy as np
import math
import tf
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from apriltags2_ros.msg import AprilTagDetectionArray

class Tag_listener(object):
	def __init__(self):
		self._pub_tag0 = rospy.Publisher('/tag0_info', Twist, queue_size=1)
		self._pub_tag1 = rospy.Publisher('/tag1_info', Twist, queue_size=1)

		self._sub_tag = rospy.Subscriber('/tag_detections',AprilTagDetectionArray,self._callback_tag)
		self._tag0_position = np.zeros(4, dtype = 'float64')
		self._tag1_position = np.zeros(4, dtype = 'float64')
		self._listener = tf.TransformListener()
	

	def _callback_tag(self,messege):
		if len(messege.detections) > 0:	
			angle_q = messege.detections[0].pose.pose.pose.orientation
			angle_r = self._change_angle([angle_q.x,angle_q.y,angle_q.z,angle_q.w])
			if(messege.detections[0].id[0] == 0):
				self._tag0_position[0] = messege.detections[0].pose.pose.pose.position.x
				self._tag0_position[1] = messege.detections[0].pose.pose.pose.position.y
				self._tag0_position[2] = messege.detections[0].pose.pose.pose.position.z
				self._tag0_position[3] = math.degrees(angle_r[2])
			elif(messege.detections[0].id[0] == 1):
				self._tag1_position[0] = messege.detections[0].pose.pose.pose.position.x
				self._tag1_position[1] = messege.detections[0].pose.pose.pose.position.y
				self._tag1_position[2] = messege.detections[0].pose.pose.pose.position.z
				self._tag1_position[3] = math.degrees(angle_r[2])
			
			rospy.loginfo("x0 : %s",self._tag0_position[0])
			rospy.loginfo("y0 : %s",self._tag0_position[1])
			rospy.loginfo("z0 : %s",self._tag0_position[2])

			rospy.loginfo("x1 : %s",self._tag1_position[0])
			rospy.loginfo("y1 : %s",self._tag1_position[1])
			rospy.loginfo("z1 : %s",self._tag1_position[2])
	
			try:
				(trans0,rot0) = self._listener.lookupTransform('tag0', 'usb_cam', rospy.Time(0))				
				(trans1,rot1) = self._listener.lookupTransform('tag1', 'usb_cam', rospy.Time(0))
				rot00 = self._change_angle(rot0)
				rot11 = self._change_angle(rot1)
#				print trans0
				print trans1
				print "\n"	
				trans0_0 = trans0
				trans0_0[0] = trans0[0]
				trans0_0[1] = trans0[1]
				trans0_0[2] = trans0[2]
		 
				a = math.radians(90) -  (math.radians(180) + rot00[0])

				tag00_info = Twist()
				tag00_info.linear.x = trans0_0[0]
				tag00_info.linear.y = trans0_0[1]
				tag00_info.linear.z = trans0_0[2] 
				tag00_info.angular.x = a
				tag00_info.angular.y = rot00[1]
				tag00_info.angular.z = rot00[2]
				self._pub_tag0.publish(tag00_info)				

				tag11_info = Twist()
				tag11_info.linear.x = trans1[0]
				tag11_info.linear.y = trans1[1]
				tag11_info.linear.z = trans1[2]
				tag11_info.angular.x = rot11[0]
				tag11_info.angular.y = rot11[1]
				tag11_info.angular.z = rot11[2] 
				self._pub_tag1.publish(tag11_info)							
			except(tf.LookupException, tf.ConnectivityException,tf.ExtrapolationException):
				pass 	

		else:
			print "nothing"

	def _change_angle(self,quaternion):
        #External parameters
		e = tf.transformations.euler_from_quaternion(quaternion)    #change angle
		return e


if __name__ == "__main__":
    tag_listener = Tag_listener()
    rospy.init_node('tag_listener')	
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
