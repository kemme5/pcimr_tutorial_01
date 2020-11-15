#!/usr/bin/env python3

import rospy
import numpy as np
from threading import Lock

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point
from pcimr_simulation.srv import InitPos

class NaiveMazeNode:

    def __init__(self):
	# Initialize Service Call
        rospy.wait_for_service('init_pos')
        try:
            s = rospy.ServiceProxy('init_pos', InitPos)
            a = int(input("Set your x goal: "))
            b = int(input("Set your y goal: "))
            s_1 = s(a , b)
            #Make sure the inserted goal position is Valid
            while str(s_1) != str("success: True"):
            	print("Goal is unreachable enter coordinates again")
            	a = int(input("Set your x goal: "))
            	b = int(input("Set your y goal: "))
            	s_1 = s(a , b)
      
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
            
        # Subscribe to Robot position and Sensor data
        self.sub_robot_position = rospy.Subscriber('/robot_pos', Point, self.cb_position)
        self.sub_scan = rospy.Subscriber('/scan', LaserScan, self.cb_scan)

        # Publish the move command (N,S,E,W)
        self.pub_move = rospy.Publisher('/move', String, queue_size = 10)

        
        
        self.move_msg = ""
        self.robot_position = Point()
        self.rangesD = 0
        self.rangesL = 0
        self.rangesT = 0
        self.rangesR = 0

    def cb_position(self, msg):
        self.robot_position.x = msg.x
        self.robot_position.y = msg.y
    
    def cb_scan(self, msg):
       
        self.rangesD = msg.ranges[0]
        self.rangesL = msg.ranges[1]
        self.rangesT = msg.ranges[2]
        self.rangesR = msg.ranges[3]

        

    def run(self, rate: float = 1):

        while not rospy.is_shutdown():

            if rate:
                if(self.robot_position.x == 16 and self.robot_position.y == 12):
                    print("I reached the Goal you can end the program")
                    rospy.sleep(1/rate)
                else:
                    if(self.rangesT != 1):
                        self.move_msg = "N"
                        print("Moving North")
                        print()
                        self.pub_move.publish(self.move_msg)
                        rospy.sleep(1/rate)
                    else:
                        self.move_msg = "E"
                        print("Found wall moving east")
                        print()
                        self.pub_move.publish(self.move_msg)
                        rospy.sleep(1/rate)
    
if __name__ == "__main__":
    rospy.init_node('naive_maze_node')
    naive_maze_node = NaiveMazeNode()
    naive_maze_node.run(rate = 1)
