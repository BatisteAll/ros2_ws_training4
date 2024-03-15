from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument


def generate_launch_description():

    return LaunchDescription([

        Node(
            package="ur10_demo_mouvment",
            executable="command_shell_robot.py",
            name="command_shell_robot",
            output="screen",
        )
    ])
    