#!/usr/bin/env python3

import rospy
import numpy as np
from threading import Lock

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point
from pcimr_simulation.srv import InitPos

class SimpleLogicNode:

    def __init__(self):

        # Subscribe to Robot position and Sensor data
        self.sub_robot_position = rospy.Subscriber('/robot_pos', Point, self.cb_position)
        self.sub_scan = rospy.Subscriber('/scan', LaserScan, self.cb_scan)

        # Publish the move command (N,S,E,W)
        self.pub_move = rospy.Publisher('/move', String, queue_size = 10)

        # Initialize Service Call
        rospy.wait_for_service('init_pos')
        try:
            s = rospy.ServiceProxy('init_pos', InitPos)
            s_1 = s(2 , 0)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
        
        self.move_msg = ""
        self.robot_position = Point()
        self.rangesX = 0
        self.rangesY = 0

    def cb_position(self, msg):
        self.robot_position.x = msg.x
        self.robot_position.y = msg.y
    
    def cb_scan(self, msg):
        self.rangesX = msg.ranges[1]
        self.rangesY = msg.ranges[2]

        

    def run(self, rate: float = 1):

        while not rospy.is_shutdown():

            if rate:
                if(self.robot_position.x == 16 and self.robot_position.y == 12):
                    print("I reached the Goal you can end the program")
                    rospy.sleep(1/rate)
                else:
                    if(self.rangesY != 1):
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
    rospy.init_node('simple_logic_node')
    simple_logic_node = SimpleLogicNode()
    simple_logic_node.run(rate = 1)
