#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Bool

def cb(x):
    rospy.loginfo(x)
def listener():


    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("to", Bool, cb)
    rospy.spin()

if __name__ == '__main__':
    listener()

