import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pow, atan2, sqrt, pi, atan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point


velval = Twist()


def updateVel(data):
    velval.linear.x= data.linear.x

    velval.angular.z= data.angular.z
    print(velval)

def updateScan(msg):
    # values at 0 degree
    if(msg.ranges[122]>0.0):
        print(msg.ranges[122])




def node():

    rospy.init_node('tut2_controller', anonymous = True)
    rate = rospy.Rate(1)

    sub_vel = rospy.Subscriber('/cmd_vel', Twist, updateVel)
    sub_scan = rospy.Subscriber('/scan', LaserScan, updateScan)

    pub_move = rospy.Publisher('/pioneer/cmd_vel', Twist, queue_size = 10)
    pub_move.publish(velval)

    rospy.spin()

if __name__ == '__main__':
    
    node()



