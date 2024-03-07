import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir

# launch permettant de lancer la simulation gazebo
def generate_launch_description():

    robot_ip = LaunchConfiguration("robot_ip")
    use_fake_hardware = LaunchConfiguration("use_fake_hardware")
    fake_sensor_commands = LaunchConfiguration("fake_sensor_commands")
    initial_joint_controller = LaunchConfiguration("initial_joint_controller")
    activate_joint_controller = LaunchConfiguration("activate_joint_controller")

    start_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory("ur_robot_driver"), 'launch', 'ur10.launch.py'
        )]),
        launch_arguments={
            "ur_type": "ur10",
            "robot_ip": robot_ip,
            "use_fake_hardware": use_fake_hardware,
            "fake_sensor_commands": fake_sensor_commands,
            "initial_joint_controller": initial_joint_controller,
            "activate_joint_controller": activate_joint_controller,
        }.items(),
    )
   
    return LaunchDescription([
        start_world,
    ])