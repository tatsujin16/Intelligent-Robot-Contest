#!/usr/bin/env python

import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16
from operator import itemgetter


class Robot_coordinates(object):
	def __init__(self):
		self._pub_ballxy1 = rospy.Publisher('/ball_xy1', Twist, queue_size=1)
		self._pub_goal_theta = rospy.Publisher('/goal_theta', Twist, queue_size=1)

		self._sub_tag0 = rospy.Subscriber('/tag0_info', Twist, self._callback_tag0)
		self._sub_tag1 = rospy.Subscriber('/tag1_info', Twist, self._callback_tag1)
		self._sub_redxy = rospy.Subscriber('red_xy', Twist, self._callback_colorxy, 'red')
		self._sub_bluexy = rospy.Subscriber('blue_xy', Twist, self._callback_colorxy, 'blue')
		self._sub_yellowxy = rospy.Subscriber('yellow_xy', Twist, self._callback_colorxy, 'yellow')
		self._sub_wait_ball = rospy.Subscriber('/wait_ball', Int16, self._callback_arduino)
		self._sub_temporary = rospy.Subscriber('/temporary', Int16, self._callback_temporary_goal)
		self._sub_practice = rospy.Subscriber('/rotation', Int16, self._callback_rotation)

		self._cam_posi = np.zeros(3, dtype = 'float32')
		self._local_robot_posi = np.zeros(3, dtype = 'float32')
		self._global_robot_posi = np.zeros(3, dtype = 'float32')
		self._global_robot_theta = np.zeros(3, dtype = 'float32')
		self._tag0_angle_r = np.zeros(3, dtype = 'float64')
		self._tag1_angle_r = np.zeros(3, dtype = 'float64')
		self._all_ball = [[0,0,0,0,0] for i in range(1,16)]
		self._arm_to_goal_theta = np.zeros(3, dtype = 'float64')
		self._goal_hozon = np.zeros(1, dtype = 'float64')
		self._goal = [[0,0] for i in range(1,5)]
		self._aho = np.zeros(3, dtype = 'float32')
		self._vacuum_posi = np.zeros(3, dtype= 'float64')

		self._goal[1] = [0.87, 0.24]
		self._goal[2] = [0.87, -1.06]
	#	self._goal[3] = [0.86, -0.405]
		self._goal[3] = [0.87, -0.41]


	def _Squaring(self, x, y):
		Shaded = np.sqrt(x*x + y*y)
		return Shaded
	
	def _callback_colorxy(self, message, name):
		global red_sh,red_TH, blue_sh,blue_TH, yellow_sh,yellow_TH, A,B,C
		if(name == 'red'):
			if(A == 5):
				A = 0
			self._redxy_X = message.linear.x
			self._redxy_Y = message.linear.y + 0.3
			self._redxy_S = message.angular.z
			red_sh = self._Squaring(self._redxy_X, self._redxy_Y)
			red_TH = self._change(self._redxy_X, self._redxy_Y)
			if(message.linear.x == 0  and message.linear.y == 0):
				self._redxy_S = red_sh = red_TH = 10 			
			self._all_ball[A][0] = self._redxy_S
			self._all_ball[A][1] = round(red_sh,2)			
			self._all_ball[A][2] = round(red_TH,2)
			self._all_ball[A][3] = 1		#red = 1
			self._all_ball[A][4] = A+1		#ball number
			A = A + 1
		elif(name == 'blue'):
			if(B == 10):
				B = 5
			self._bluexy_X = message.linear.x
			self._bluexy_Y = message.linear.y + 0.3				
			self._bluexy_S = message.angular.z
			blue_sh = self._Squaring(self._bluexy_X, self._bluexy_Y)
			blue_TH = self._change(self._bluexy_X, self._bluexy_Y)
			if(message.linear.x == 0 and message.linear.y == 0):
				self._bluexy_S = blue_sh = blue_TH = 10
			self._all_ball[B][0] = self._bluexy_S
			self._all_ball[B][1] = round(blue_sh,2)
			self._all_ball[B][2] = round(blue_TH,2)
			self._all_ball[B][3] = 2		#blue = 2
			self._all_ball[B][4] = B-4
			B = B + 1
		elif(name == 'yellow'):
			if(C == 15):
				C = 10 
			self._yellowxy_X = message.linear.x
			self._yellowxy_Y = message.linear.y + 0.3
			self._yellowxy_S = message.angular.z
			yellow_sh = self._Squaring(self._yellowxy_X, self._yellowxy_Y)
			yellow_TH = self._change(self._yellowxy_X, self._yellowxy_Y)
			if(message.linear.x == 0 and message.linear.y == 0):
				self._yellowxy_S = yellow_sh = yellow_TH = 10
			self._all_ball[C][0] = self._yellowxy_S
			self._all_ball[C][1] = round(yellow_sh,2)
			self._all_ball[C][2] = round(yellow_TH,2)
			self._all_ball[C][3] = 3		#yellow = 3
			self._all_ball[C][4] = C-9
			C = C + 1

		self._Replacement = self._all_ball
		self._Replacement.sort(key=itemgetter(0))
		print self._Replacement
		print "\n"

	def _callback_arduino(self, message):
		global tooi
		judgment = message.data
		if(judgment == 1):
			if(self._vacuum_posi[0] < -0.50):
				tooi = 1
			else:
				tooi = 0
			ball_xy1 = Twist()
			ball_xy1.linear.x = (self._Replacement[0][1])*100 - 31
			ball_xy1.linear.z = self._Replacement[0][3]
			ball_xy1.angular.x = tooi
			ball_xy1.angular.z = round(math.degrees(self._Replacement[0][2])) 
			self._pub_ballxy1.publish(ball_xy1)
		else:
			pass	
		
	def _callback_tag0(self, message):
		self._cam_posi[0] = message.linear.x
		self._cam_posi[1] = message.linear.y
		self._cam_posi[2] = message.linear.z
		self._tag0_angle_r[2] = message.angular.z
	
	def _callback_tag1(self, message):
		self._local_robot_posi[0] = message.linear.x  
		self._local_robot_posi[1] = message.linear.y - 0.10 
		self._local_robot_posi[2] = message.linear.z
		self._tag1_angle_r[2] = message.angular.z
		self._vacuum posi[2] = self._local_robot_posi[1] - 0.3
		
		self._global_robot_posi[0], self._global_robot_posi[1] = self._Transform(self._local_robot_posi[0], self._local_robot_posi[1])
		self._vacuum_posi[0], self._vacuum_posi[1] = self._Transform(self._local_robot_posi[0], self._vacuum_posi[2])
		self._global_robot_theta[2] = self._tag0_angle_r[2] - self._tag1_angle_r[2]  

	def _make_rot_mat(self, angle):
		rot_matrix = [[np.cos(angle),np.sin(angle)],[(-1)*np.sin(angle),np.cos(angle)]]
		rot_matrix = np.matrix(rot_matrix)
		return rot_matrix

	def _Transform(self, XXX, YYY):
		from_tag1_to_camera = np.array([XXX, YYY])
		from_tag0_to_camera = np.matrix([[self._cam_posi[0]],[self._cam_posi[1]]])
		rot_mat = self._make_rot_mat(self._tag1_angle_r[2] - self._tag0_angle_r[2])
		rot_xy = np.dot(rot_mat, from_tag1_to_camera.reshape(2,1))
		from_tag0_to_tag1 = from_tag0_to_camera - rot_xy
		para_rot_x, para_rot_y = from_tag0_to_tag1[0,0], from_tag0_to_tag1[1,0]
		return para_rot_x, para_rot_y

	def _change(self, x, y):
		global shitaa
		if(x>0 and y>0):
			shitaa = math.radians(90) - math.atan2(y, x)
		elif(x<0 and y>0):
			a = (-1)*x
			shitaa = (-1)*(math.radians(90) - math.atan2(y, a)) 
		elif(x>0 and y<0):
			b = (-1)*y
			shitaa = math.radians(90) + math.atan2(b, x)
		elif(x<0 and y<0):
			a = (-1)*x
			b = (-1)*y
			shitaa = (-1)*(math.radians(90) + math.atan2(b, a))
		return shitaa			
		
	def _callback_temporary_goal(self, message):
		color = message.data
		arm_X = np.array([self._global_robot_posi[0], self._global_robot_posi[1]])
		para_X = self._goal[color] - arm_X
		rot_mat = self._make_rot_mat(self._global_robot_theta[2])
		rot_xy = np.dot(rot_mat, para_X.reshape(2,1))	
		para_rot_X, para_rot_Y = rot_xy[0,0], rot_xy[1,0]
		self._aho[0] = para_rot_X
		self._aho[1] = para_rot_Y
		self._aho[2] = self._Squaring(self._aho[0], self._aho[1])
		self._goal[0] = self._change(para_rot_X, para_rot_Y)
#		print self._aho[2]

	def _callback_rotation(self, message):
		global more_angle
		judgement1 = message.data
		GOAL_THETA = round(math.degrees(self._goal[0]))
		if(self._aho[2] > 1.60 and self._aho[2] < 1.80):
			more_angle = 1
		else:
			more_angle = 0 
#		print more_angle
#		print self._aho[0]
#		print self._aho[1]
#		print '\n'
#		print GOAL_THETA
		if(judgement1 == 1):
			goal_theta = Twist()
			goal_theta.linear.x = GOAL_THETA
			goal_theta.angular.x = more_angle
			self._pub_goal_theta.publish(goal_theta)
		else:
			pass


if __name__ == '__main__':
	rospy.init_node('robot_position')
	Robot_coordinates = Robot_coordinates()
	try:
		A = 0
		B = 5
		C = 10
		rospy.spin()
	except KeyboardInterrupt:
		pass
