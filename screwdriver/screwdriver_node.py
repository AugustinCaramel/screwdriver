import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ScrewdriverNode(Node):
    def __init__(self):
        super().__init__('screwdriver_node')
        self.publisher_ = self.create_publisher(String, 'screwdriver_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Screwdriver node started')

    def timer_callback(self):
        msg = String()
        msg.data = 'running'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = ScrewdriverNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()