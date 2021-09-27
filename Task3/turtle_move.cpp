#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
ros::Publisher velocity_publisher;

using namespace std;

void move(double speed,double distance,bool isForward);

int main(int argc,char **argv)

{
    ros::init(argc,argv,"turtle_mover");
    ros::NodeHandle n;

    double speed;
    double distance;
    bool isForward;
    
    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmdvel",10);

    cout<<"enter speed";
    cin>>speed;
    cout<<"enter distance";
    cin>>distance;
    cout<<"enter direction";
    cin>>isForward;


    move(speed,distance,isForward);
}

void move(double speed,double distance,bool isForward)
{
    geometry_msgs::Twist vel_msg;

    if(isForward)
        vel_msg.linear.x=abs(speed);
    else
        vel_msg.linear.x=-abs(speed);

    vel_msg.linear.y=0;
    vel_msg.linear.z=0;

    vel_msg.angular.x=0; 
    vel_msg.angular.y=0;
    vel_msg.angular.z=0;

    double t0=ros::Time::now().toSec();

    double current_distance=0;

    ros::Rate loop_rate(10);

    do{
        velocity_publisher.publish(vel_msg);
        double t1=ros::Time::now().toSec();
        current_distance=speed*(t1-t0);
        ros::spinOnce();
        loop_rate.sleep();

    }while(current_distance<distance);
    vel_msg.linear.x=0;
    velocity_publisher.publish(vel_msg);  
}