import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class pub_node(Node):
    def __init__(self):
        super().__init__("pub_node")
        self.publisher = self.create_publisher(String,"topic",10)
        time = 0.5
        self.timer = self.create_timer(time,self.timer_callback)
    
    def timer_callback(self):
        msg = String()
        msg.data = "Hello! ROS2 is fun"
        self.publisher.publish(msg)
        self.get_logger().info(f"publishing {msg.data}")



def main(args=None):
    rclpy.init(args=args)
    pub=pub_node()
    rclpy.spin(pub)
    rclpy.shutdown()


if __name__ == "__main__":
    main()