import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class sub_node(Node):
    def __init__(self):
        super().__init__("sub_node")
        self.subscriber = self.create_subscription(String,"topic",self.sub_callback,10)
    def sub_callback(self,msg):
        self.get_logger().info(f"Reciever {msg.data}")



def main(args=None):
    rclpy.init(args=args)
    sub=sub_node()
    rclpy.spin(sub)
    sub.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
