#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration
import argparse
import time
import sys

class JointTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('joint_trajectory_publisher')
        self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.get_logger().info('Le nœud de publication de la trajectoire des joints a été créé.')

    def publish_trajectory(self, joint_positions):
        joint_trajectory = JointTrajectory()
        joint_trajectory.header = Header(stamp=self.get_clock().now().to_msg(), frame_id="base_link")
        joint_trajectory.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

        trajectory_point = JointTrajectoryPoint()
        # trajectory_point.positions = [1.57, -1.57, 0.0, 0.0, 0.0, 0.0]
        trajectory_point.positions = joint_positions
        trajectory_point.time_from_start = Duration(sec=1, nanosec=0)

        joint_trajectory.points = [trajectory_point]

        self.publisher_.publish(joint_trajectory)
        self.get_logger().info('Trajectoire des joints publiée')

def main(args=None):
    rclpy.init(args=args)

    joint_trajectory_publisher = JointTrajectoryPublisher()
    # Attendre un court instant avant de publier la trajectoire
    # time.sleep(1)
    
    # Vérification des arguments de ligne de commande
    if len(sys.argv) != 7:
        print("Usage: ros2 run command_shell_robot.py joint1 joint2 joint3 joint4 joint5 joint6")
        return
    # Conversion des arguments en float
    joint_positions = [float(arg) for arg in sys.argv[1:]]
    joint_trajectory_publisher.publish_trajectory(joint_positions)
    # joint_trajectory_publisher.publish_trajectory()

    # joint_trajectory_publisher.get_logger().info('test')
    # rclpy.spin_once(joint_trajectory_publisher)  # Attendre la publication
    # joint_trajectory_publisher.get_logger().info('fin')

    joint_trajectory_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()