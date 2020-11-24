import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pow, atan2, sqrt, pi, atan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point


class bot:
    
    def __init__(self):
        self.command = Twist()
        self.sense = 0
        self.sub_vel = rospy.Subscriber('/cmd_vel', Twist, self.updateVel)
        self.sub_scan = rospy.Subscriber('/scan', LaserScan, self.updateScan)

    def updateVel(self,data):
        self.command.linear.x = data.linear.x
        self.command.angular.z = data.angular.z
    def updateScan(self,msg):
        self.sense = msg.ranges[122] #this is the mid value so middle of robot
    
    




def node():

    rospy.init_node('tut2_controller', anonymous = True)
    rate = rospy.Rate(1)
    vel_msg = Twist()
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    bot1 = bot()

    pub_move = rospy.Publisher('pioneer/cmd_vel', Twist, queue_size = 10)
    
    while not rospy.is_shutdown():
        vel_msg.linear.x = bot1.command.linear.x*bot1.sense
        if bot1.sense<0.2:
            vel.msg.linear.x = 0
            vel.msg.angular.z = 0
        vel_msg.angular.z = bot1.command.angular.z
        pub_move.publish(vel_msg)
        rate.sleep()
        

if __name__ == '__main__':
    try:
         node()
         rospy.spin()
    except rospy.ROSInterruptException: pass



