#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Char

def cb(data):
    rospy.loginfo('I heard %c', data.data)
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("to", Char, cb)
    rospy.spin()

if __name__ == '__main__':
    listener()
