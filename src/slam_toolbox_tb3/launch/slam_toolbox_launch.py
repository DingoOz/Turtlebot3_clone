import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time")
    slam_params_file = LaunchConfiguration("slam_params_file")

    # Set a default value for LDS_MODEL if it's not already set
    lds_model = EnvironmentVariable("LDS_MODEL", default_value="A1")

    declare_use_sim_time_argument = DeclareLaunchArgument(
        "use_sim_time", default_value="false", description="Use simulation/Gazebo clock"
    )
    declare_slam_params_file_cmd = DeclareLaunchArgument(
        "slam_params_file",
        default_value=os.path.join(
            get_package_share_directory("slam_toolbox_tb3"), "config", "slam_toolbox_params.yaml"
        ),
        description="Full path to the ROS2 parameters file to use for the slam_toolbox node",
    )

    start_async_slam_toolbox_node = Node(
        parameters=[slam_params_file, {"use_sim_time": use_sim_time}],
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        name="slam_toolbox",
        output="screen",
    )

    ld = LaunchDescription()

    # ld.add_action(SetEnvironmentVariable('LDS_MODEL', lds_model))
    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_slam_params_file_cmd)
    ld.add_action(start_async_slam_toolbox_node)

    return ld
