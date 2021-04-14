#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

move = Twist()

def auto_move():
    rospy.Subscriber("/robot/laser_scan", LaserScan, callback)
    rospy.spin()

rospy.init_node("auto_move", anonymous = True)
pub = rospy.Publisher("/robot/cmd_vel", Twist, queue_size=10)
r = rospy.Rate(10)





def callback(msg):
    min = 1000
    index = 0
    sum_left=0
    sum_right=0
    for x in range(83,417):
        if msg.ranges[x]<min:
            min = msg.ranges[x]
            index = x
    for i in range(index,667):
        sum_right+=msg.ranges[i]

    for j in range(0,index):
        sum_left+=msg.ranges[j]

    if min>0.5:
        move.linear.x = 0.3
        move.angular.z = 0
        pub.publish(move)
        r.sleep()
    else:
        if sum_right>sum_left:
            move.linear.x = 0
            move.angular.z = 0.3
            pub.publish(move)
            r.sleep()
        else:
            move.linear.x = 0
            move.angular.z = -0.3
            pub.publish(move)
            r.sleep()



#    j=344
    #for i in range(320,500):
        #if msg.ranges[i]<0.8:
        #if msg.ranges[i]<0.8:
#    if msg.ranges[j]>0.5:
#            move.linear.x = 0.3
#            move.angular.z = 0
#    else:
#        j+=10
#        if msg.ranges[j]<0.5:
#            move.linear.x = 0
#            move.angular.z = 0.7
#        pub.publish(move)
#        r.sleep()
        #break
#    pub.publish(move)
#    r.sleep()

#if __name__=="__main__":
#    try:
#        auto_move()
#    except rospy.ROSInterruptException:
#        pass
if __name__=="__main__":
    try:
        auto_move()
    except rospy.ROSInterruptException:
        pass
