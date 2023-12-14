improt rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

relpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

