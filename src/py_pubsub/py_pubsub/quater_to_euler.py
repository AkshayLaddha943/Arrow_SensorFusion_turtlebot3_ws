import rclpy
from rclpy.node import Node
from math import *
from nav_msgs.msg import Odometry
import tf_transformations

class PoseSubscriber(Node):

    def __init__(self):
        super().__init__('Pose_subscriber')
        self.subscription = self.create_subscription(Odometry, '/odom', self.get_rotation, 10)
          
        self.publisher_ = self.create_publisher(Odometry, '/euler_odom', 10)
        self.subscription
        
    def publish_value(self):
        msg = Odometry()
        
    def get_rotation(self, msg):
        global roll, pitch, yaw
        orientation_mat = msg.pose.pose.orientation
        orientation_list = [orientation_mat.x, orientation_mat.y, orientation_mat.z, orientation_mat.w]
        (roll, pitch, yaw) = tf_transformations.euler_from_quaternion(orientation_list)
        print("roll: ",roll, "pitch: ",pitch, "yaw: ",yaw)
        #self.publisher_.publish(newangle)
            
        
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = PoseSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
