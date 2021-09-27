#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Char

def ty():
    pub = rospy.Publisher('to', Char, queue_size=10)
    rospy.init_node('talker1')
    r = rospy.Rate(10) # 1hz
    char = 'a'
    i=0
    while not rospy.is_shutdown():
        

        print(char)
        pub.publish(i)
        r.sleep()
        i=ord(char[0])
        i+=1
        char=chr(i)
        if char=='{':
            char='a'

if __name__ == '__main__':
    try:
        ty()
    except rospy.ROSInterruptException:
        pass
