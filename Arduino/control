#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyTwist(object):
	def __init__(self):
		self._joy_sub = rospy.Subscriber('joy' , Joy, self._joy_callback, queue_size=1)
		self._twist_pub = rospy.Publisher('/control', Twist, queue_size=10)		

	def _joy_callback(self, joy_msg):
		twist = Twist()
		twist.linear.x = joy_msg.axes[1]*10
		twist.angular.z = joy_msg.axes[2]*10
		self._twist_pub.publish(twist)
		print joy_msg.axes[1]
		print joy_msg.axes[2]


if __name__ == '__main__':
	rospy.init_node('joy_twist')
	joy_twist = JoyTwist()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
