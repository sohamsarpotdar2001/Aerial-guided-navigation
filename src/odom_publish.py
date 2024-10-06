#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import LinkStates
from nav_msgs.msg import Odometry
import tf.transformations
import tf2_ros
from geometry_msgs.msg import Point, Quaternion, Pose, Twist, Vector3, TransformStamped

class odom_pub():
    def __init__(self):
        rospy.init_node('drone_odom')
        self.camera_sub = rospy.Subscriber('/gazebo/link_states', LinkStates, self.posecallback)
        self.odom_pub = rospy.Publisher('/robot2/odom', Odometry, queue_size=10)
        self.vel_pub = rospy.Publisher('/robot2/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.odom_broadcaster = tf2_ros.TransformBroadcaster()
        self.tf = TransformStamped()
        self.publishing = False
        self.quat = tf.transformations.quaternion_from_euler(0,0,0)
        # self.position = Vector3(0,0,0)
        self.orientation = Quaternion(*self.quat)
        # self.linear = Vector3(0,0,0)
        # self.angular = Vector3(0,0,0)
    
    def posecallback(self,msg):
        if len(msg.pose) > 5:
            self.publishing = True
            self.position = msg.pose[5].position 
            # self.orientation = msg.pose[5].orientation
            self.linear = msg.twist[5].linear
            self.angular = msg.twist[5].angular
    
    def convert_nsecs_to_int(self,nsecs):
        if len(str(nsecs)) > 9:
            b = pow(10,(len(str(nsecs)) - 9)) 
            nsecs = nsecs / b
            return int(nsecs)
        else :
            return int(nsecs)
                   
    def publish_odom(self):
        odom = Odometry()
        vel = Twist()
        while not rospy.is_shutdown():
            if self.publishing:
                current_time = rospy.Time.now()
                
                self.tf.header.frame_id = 'robot2_tf/odom'
                self.tf.child_frame_id = 'robot2_tf/base_link'
                self.tf.header.stamp = current_time
                # self.tf.header.stamp.secs = current_time.to_sec()
                # self.tf.header.stamp.nsecs = current_time.to_nsec()
                self.tf.transform.translation.x = self.position.x
                self.tf.transform.translation.y = self.position.y
                self.tf.transform.translation.z = self.position.z
                self.tf.transform.rotation = self.orientation
                self.odom_broadcaster.sendTransform(self.tf)

                odom.header.frame_id = 'robot2_tf/odom'            
                odom.child_frame_id = 'robot2_tf/base_link'
                odom.header.stamp.secs = int(current_time.to_sec())
                odom.header.stamp.nsecs = self.convert_nsecs_to_int(current_time.to_nsec())
                odom.pose.pose.position = self.position
                odom.pose.pose.orientation = self.orientation           
                odom.twist.twist.linear = self.linear
                odom.twist.twist.angular = self.angular
                
                vel.linear = self.linear
                vel.angular = self.angular

                self.odom_pub.publish(odom)
                self.vel_pub.publish(vel)
                self.rate.sleep()
            else:
                pass

if __name__ == '__main__':
    try:
        odom_publish = odom_pub()
        odom_publish.publish_odom()
    except KeyboardInterrupt:
        pass