#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Num

def talker():
    pub = rospy.Publisher('custom_chatter', Num,queue_size=10)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Num()
    #msg.name = "ROS User"
    msg.age = 4

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
