#!/usr/bin/env python3

from socket import MsgFlag
from turtle import pu
from numpy import rate
import rospy
from geometry_msgs.msg import Twist
# from turtlesim.msg import Color

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        # publish cmd vel
        msg = Twist()
        msg.linear.x = 3.0
        msg.angular.z = 2.0
        # msg.angular.y = 0.5
        pub.publish(msg)
        rate.sleep()

    # rospy.init_node("color_background")
    # rospy.loginfo("Node has been changed color")

    # pub = rospy.Publisher("/turtle1/color_sensor", Color, queue_size=4)

    # rate = rospy.Rate(50)

    # while not rospy.is_shutdown():
    #     msg = Color()
    #     msg.r = 30
    #     msg.g = 0
    #     msg.b = 30
    #     pub.publish(msg)
    #     print(msg)
    #     rate.sleep()


    #phan nay sai vi no dinh nghia la subcriber chu khong phai la publisher

