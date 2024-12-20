import os
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage, Image
from cv_bridge import CvBridge
import cv2


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        self.bridge = CvBridge()
        # Directories to save the frames
        self.RGB_frames_folder = '/home/frames/RGB-camera'
        self.SWIR_frames_folder = '/home/frames/SWIR'
        os.makedirs(self.RGB_frames_folder, exist_ok=True)
        os.makedirs(self.SWIR_frames_folder, exist_ok=True)

        # Frame counters and drop settings
        self.frame_count_compressed = 0
        self.frame_count_uncompressed = 0
        self.drop_rate = 2  # Save one frame every 'drop_rate' frames

        # Subscriptions for compressed and uncompressed image topics
        self.subscription_rgb = self.create_subscription(
            CompressedImage,
            '/allied_swir/image_raw/compressed',
            self.callback_rgb,
            10
        )

        self.subscription_swir = self.create_subscription(
            CompressedImage,
            '/allied_rgb/image_raw/compressed',
            self.callback_swir,
            10
        )

    def callback_rgb(self, msg):
        if self.frame_count_compressed % self.drop_rate != 0:
            self.frame_count_compressed += 1
            return

        try:
            # Convert the compressed image to an OpenCV image
            img_uncomp = self.bridge.compressed_imgmsg_to_cv2(msg)
            img_uncomp = cv2.rotate(img_uncomp, cv2.ROTATE_180)

            # Create the file path for this frame
            frame_path = os.path.join(self.RGB_frames_folder, f'compressed_frame_{self.frame_count_compressed:06d}.jpg')

            # Save the frame as an image
            cv2.imwrite(frame_path, img_uncomp)
            self.get_logger().info(f"Saved compressed frame to {frame_path}")

            # Increment the frame counter
            self.frame_count_compressed += 1
        except Exception as e:
            self.get_logger().error(f"Error processing compressed frame: {e}")

    def callback_swir(self, msg):
        if self.frame_count_compressed % self.drop_rate != 0:
            self.frame_count_compressed += 1
            return

        try:
            # Convert the compressed image to an OpenCV image
            img_uncomp = self.bridge.compressed_imgmsg_to_cv2(msg)
            img_uncomp = cv2.rotate(img_uncomp, cv2.ROTATE_180)

            # Create the file path for this frame
            frame_path = os.path.join(self.RGB_frames_folder, f'compressed_frame_{self.frame_count_compressed:06d}.jpg')

            # Save the frame as an image
            cv2.imwrite(frame_path, img_uncomp)
            self.get_logger().info(f"Saved compressed frame to {frame_path}")

            # Increment the frame counter
            self.frame_count_compressed += 1
        except Exception as e:
            self.get_logger().error(f"Error processing compressed frame: {e}")

    def exit_handler(self):
        self.get_logger().info(f"Frames saved successfully to {self.RGB_frames_folder} and {self.SWIR_frames_folder}")


def main(args=None):
    rclpy.init(args=args)

    subscriber_image = MinimalSubscriber()

    try:
        rclpy.spin(subscriber_image)
    except KeyboardInterrupt:
        subscriber_image.exit_handler()
        subscriber_image.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
