#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move_hex():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    for i in range(6):
        vel_msg.linear.x = 1
        #Since we are moving just in x-axis
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        while not rospy.is_shutdown():

                #Setting the current time for distance calculus
                t0 = rospy.Time.now().to_sec()
                current_distance = 0

                #Loop to move the turtle in an specified distance
                while(current_distance < 2):
                    #Publish the velocity
                    velocity_publisher.publish(vel_msg)
                    #Takes actual time to velocity calculus
                    t1=rospy.Time.now().to_sec()
                    #Calculates distancePoseStamped
                    current_distance= 1*(t1-t0)
                #After the loop, stops the robot
                break    
        angular_speed = float(30*2*math.pi/360)
        relative_angle = float(60*2*math.pi/360)

        #We wont use linear components
        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0

        # Checking if our movement is CW or CCW
        
        vel_msg.angular.z = abs(angular_speed)
        # Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)
        
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        # Testing our function
        move_hex()
    except rospy.ROSInterruptException:
        pass