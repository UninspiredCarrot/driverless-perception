import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from eufs_msgs.msg import ConeArrayWithCovariance, ConeWithCovariance
from cv_bridge import CvBridge
import numpy as np
from . import process_frame

class ConeDetectionNode(Node):
    def __init__(self):
        super().__init__('cone_detection_node')
        self.left_image = None
        self.right_image = None
        self.subscription_left = self.create_subscription(
            Image,
            'rectified_left_image',
            self.left_image_callback,
            10)
        self.subscription_right = self.create_subscription(
            Image,
            'rectified_right_image',
            self.right_image_callback,
            10)
        self.publisher = self.create_publisher(
            ConeArrayWithCovariance,
            'cone_array_with_covariance',
            10)
        self.bridge = CvBridge()

    def left_image_callback(self, msg):
        self.left_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.detect_and_publish_cones()

    def right_image_callback(self, msg):
        self.right_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.detect_and_publish_cones()

    def detect_and_publish_cones(self):
        if self.left_image is not None and self.right_image is not None:
            cone_positions = process_frame.process(self.left_image, self.right_image)
            if cone_positions:
                cone_msg = self.construct_cone_message(cone_positions)
                self.publisher.publish(cone_msg)

    def construct_cone_message(self, cone_positions):
        cone_msg = ConeArrayWithCovariance()
        cone_msg.header.stamp = self.get_clock().now().to_msg()

        for cone in cone_positions:
            cone_with_covariance = ConeWithCovariance()
            cone_with_covariance.point.x = cone['x']
            cone_with_covariance.point.y = cone['y']
            cone_with_covariance.covariance = np.zeros((2, 2)).flatten().tolist()
            if cone['type'] == 'blue_cone':
                cone_msg.blue_cones.append(cone_with_covariance)
            elif cone['type'] == 'yellow_cone':
                cone_msg.yellow_cones.append(cone_with_covariance)
            elif cone['type'] == 'orange_cone':
                cone_msg.orange_cones.append(cone_with_covariance)
            elif cone['type'] == 'big_orange_cone':
                cone_msg.big_orange_cones.append(cone_with_covariance)
            elif cone['type'] == 'unknown_color_node':
                cone_msg.unknown_color_cones.append(cone_with_covariance)

        return cone_msg

def main(args=None):
    rclpy.init(args=args)
    node = ConeDetectionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
