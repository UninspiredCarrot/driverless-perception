import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from . import zed_opencv_native
import cv2

class ZedCameraNode(Node):
    def __init__(self):
        super().__init__('zed_camera_node')
        self.publisher_left_raw = self.create_publisher(Image, 'raw_left_image', 10)
        self.publisher_right_raw = self.create_publisher(Image, 'raw_right_image', 10)
        self.publisher_left_rect = self.create_publisher(Image, 'rectified_left_image', 10)
        self.publisher_right_rect = self.create_publisher(Image, 'rectified_right_image', 10)
        self.bridge = CvBridge()

        self.video_capture = cv2.VideoCapture(0)


    def rectify_frame(self, frame):
        rectified_frame = zed_opencv_native.process(frame)
        return rectified_frame

    def publish_images(self, left_image_raw, right_image_raw, left_image_rect, right_image_rect):
        msg_left_raw = self.bridge.cv2_to_imgmsg(left_image_raw, 'bgr8')
        msg_right_raw = self.bridge.cv2_to_imgmsg(right_image_raw, 'bgr8')
        msg_left_rect = self.bridge.cv2_to_imgmsg(left_image_rect, 'bgr8')
        msg_right_rect = self.bridge.cv2_to_imgmsg(right_image_rect, 'bgr8')
        self.publisher_left_raw.publish(msg_left_raw)
        self.publisher_right_raw.publish(msg_right_raw)
        self.publisher_left_rect.publish(msg_left_rect)
        self.publisher_right_rect.publish(msg_right_rect)

    def capture_and_publish(self):
        ret, frame = self.video_capture.read()
        if ret:
            left_image_raw, right_image_raw = zed_opencv_native.split(frame)
            rectified_frame = self.rectify_frame(frame)
            left_image_rect, right_image_rect = zed_opencv_native.split(rectified_frame)
            self.publish_images(left_image_raw, right_image_raw, left_image_rect, right_image_rect)

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
