import rclpy
from rclpy.node import Node
from math import *
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

class OdomSubscriber(Node):

    def __init__(self):
        super().__init__('Odom_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.get_rotation,
            10)
          
        self.publisher_ = self.create_publisher(Odometry, '/odom_degree', 10)
        self.subscription  # prevent unused variable warning       
        
    def publish_value(self):
        msg = Odometry()
        
    def get_rotation(self, msg):
        self.publisher_.publish(msg)
        
        
        
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = OdomSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
    
    
    
