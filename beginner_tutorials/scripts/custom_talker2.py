#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Cred

def talker():
    pub = rospy.Publisher('custom_chatter', Cred,queue_size=10)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Cred()
    #msg.name = "ROS User"
    msg.first_name = "bruh"
    msg.last_name = "Man"
    msg.age=69
    msg.score=6969
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
