#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Bool

def ty():
    pub = rospy.Publisher('to', Bool, queue_size=10)
    rospy.init_node('talker1',anonymous=True)
    r = rospy.Rate(1) # 1hz

    bool  = True
    while not rospy.is_shutdown():
        bool = not bool
        print(bool)
        pub.publish(bool)
            
        r.sleep()                

if __name__ == '__main__':
    try:
        ty()
    except rospy.ROSInterruptException:
        pass
