import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration
import time

class JointTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('joint_trajectory_publisher')
        self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.get_logger().info('Le nœud de publication de la trajectoire des joints a été créé.')

    def publish_trajectory(self):
        joint_trajectory = JointTrajectory()
        joint_trajectory.header = Header(stamp=self.get_clock().now().to_msg(), frame_id="base_link")
        joint_trajectory.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

        trajectory_point = JointTrajectoryPoint()
        trajectory_point.positions = [1.57, -1.57, 0.0, 0.0, 0.0, 0.0]
        trajectory_point.time_from_start = Duration(sec=1, nanosec=0)

        joint_trajectory.points = [trajectory_point]

        self.publisher_.publish(joint_trajectory)
        self.get_logger().info('Trajectoire des joints publiée')

def main(args=None):
    rclpy.init(args=args)
    joint_trajectory_publisher = JointTrajectoryPublisher()

    # Attendre un court instant avant de publier la trajectoire
    time.sleep(1)

    joint_trajectory_publisher.publish_trajectory()

    rclpy.spin_once(joint_trajectory_publisher)  # Attendre la publication

    joint_trajectory_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Header
# from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

# class JointTrajectoryPublisher(Node):
#     def __init__(self):
#         super().__init__('joint_trajectory_publisher')
#         self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
#         self.timer = self.create_timer(1.0, self.publish_trajectory)
#         self.get_logger().info('Joint Trajectory Publisher Node has been created.')


#         self.tolerances = {
#             "shoulder_pan_joint": 0.1,
#             "shoulder_lift_joint": 0.1,
#             "elbow_joint": 0.1,
#             "wrist_1_joint": 0.1,
#             "wrist_2_joint": 0.1,
#             "wrist_3_joint": 0.1
#         }

#     def publish_trajectory(self):
#         joint_trajectory = JointTrajectory()
#         joint_trajectory.header = Header()
#         joint_trajectory.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

#         trajectory_point = JointTrajectoryPoint()
#         trajectory_point.positions = [0.0, -1.57, 0.0, 0.0, 0.0, 0.0]
#         # trajectory_point.velocities = []
#         # trajectory_point.accelerations = []
#         # trajectory_point.effort = []
#         # trajectory_point.time_from_start = rclpy.time.Duration(seconds=4)

#         joint_trajectory.points = [trajectory_point]

#         self.publisher_.publish(joint_trajectory)
#         self.get_logger().info('Joint Trajectory Published')

# def main(args=None):
#     rclpy.init(args=args)
#     joint_trajectory_publisher = JointTrajectoryPublisher()
#     rclpy.spin(joint_trajectory_publisher)
#     joint_trajectory_publisher.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
