import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():
    package_name ="my_bot"

    pkg_share =get_package_share_directory(package_name)


    rviz_config = os.path.join(
        pkg_share,
        "rviz",
        "robot.rviz"
    )

    rviz2 =Node (
        package="rviz2",
        exec_name="rviz2",
        arguments=[
            "-d", rviz_config
        ],
        output = "screen"
    )


    return  LaunchDescription([
        rviz2
    ])