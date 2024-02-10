import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from . import zed_opencv_native
import cv2

class ZedCameraNode(Node):
    def __init__(self):
        super().__init__('zed_camera_node')
        self.publisher_left = self.create_publisher(Image, 'rectified_left_image', 10)
        self.publisher_right = self.create_publisher(Image, 'rectified_right_image', 10)
        self.bridge = CvBridge()

        self.video_capture = cv2.VideoCapture(0)


    def rectify_frame(self, frame):
        rectified_frame = zed_opencv_native.process(frame)
        return rectified_frame

    def publish_images(self, left_image, right_image):
    
        msg_left = self.bridge.cv2_to_imgmsg(left_image, 'bgr8')
        msg_right = self.bridge.cv2_to_imgmsg(right_image, 'bgr8')
        self.publisher_left.publish(msg_left)
        self.publisher_right.publish(msg_right)

    def capture_and_publish(self):

        ret, frame = self.video_capture.read()

        if ret:

            rectified_frame = self.rectify_frame(frame)
            lf, rf = zed_opencv_native.split(rectified_frame)
            self.publish_images(lf, rf)

def main(args=None):
    rclpy.init(args=args)
    node = ZedCameraNode()
    try:
        while rclpy.ok():
            node.capture_and_publish()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
