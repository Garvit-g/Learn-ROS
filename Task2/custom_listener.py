#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Num

def callback(Data):
    rospy.loginfo("age is: %d" % (Data.age))

def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("custom_chatter", Num, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()