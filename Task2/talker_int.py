#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int16
import random

def ty():
    pub = rospy.Publisher('to', Int16, queue_size=10)
    rospy.init_node('talker1')
    r = rospy.Rate(1) # 1hz
    value=0
    while not rospy.is_shutdown():

        value=value+2
    
        print(value)
        pub.publish(value)
        r.sleep()
if __name__ == '__main__':
    try:
        ty()
    except rospy.ROSInterruptException:
        pass
        
        
        
