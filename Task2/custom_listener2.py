#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Cred

def callback(Data):
    rospy.loginfo("Name is : %s %s \n age is: %d \n Score is: %d \n" % (Data.last_name,Data.first_name,Data.age,Data.score))

def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("custom_chatter", Cred, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()