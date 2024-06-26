import launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution, EnvironmentVariable
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
  """Generate launch description for ublox_dgnss components."""
  dgnss_params = []
    #    {'CFG_USBOUTPROT_NMEA': False},
    #              {'CFG_RATE_NAV': 1},
    #              {'CFG_MSGOUT_UBX_NAV_HPPOSLLH_USB': 1},
    #              {'CFG_MSGOUT_UBX_NAV_STATUS_USB': 5},
    #              {'CFG_MSGOUT_UBX_RXM_RTCM_USB': 1}]

  use_https_arg = DeclareLaunchArgument(
    "use_https", default_value=TextSubstitution(text="true")
  )
  host_arg = DeclareLaunchArgument(
    "host", default_value=TextSubstitution(text="ppntrip.services.u-blox.com")
  )
  port_arg = DeclareLaunchArgument(
    "port", default_value=TextSubstitution(text="2102")
  )
  mountpoint_arg = DeclareLaunchArgument(
    "mountpoint", default_value=TextSubstitution(text="US")
  )
  username_arg = DeclareLaunchArgument(
    "username", default_value=EnvironmentVariable(name="NTRIP_USERNAME", default_value="noname")
  )
  password_arg = DeclareLaunchArgument(
    "password", default_value=EnvironmentVariable(name="NTRIP_PASSWORD", default_value="password")
  )
  ntrip_params = [{
    'use_https': LaunchConfiguration('use_https'),
    'host': LaunchConfiguration('host'),
    'port': LaunchConfiguration('port'),
    'mountpoint': LaunchConfiguration('mountpoint'),
    'username': LaunchConfiguration('username'),
    'password': LaunchConfiguration('password')
  }]

  container1 = ComposableNodeContainer(
    name='ublox_dgnss_container',
    namespace='',
    package='rclcpp_components',
    executable='component_container_mt',
    composable_node_descriptions=[
      ComposableNode(
        package='ublox_dgnss_node',
        plugin='ublox_dgnss::UbloxDGNSSNode',
        name='ublox_dgnss',
        parameters=dgnss_params
      ),
      ComposableNode(
        package='ntrip_client_node',
        plugin='ublox_dgnss::NTRIPClientNode',
        name='ntrip_client',
        parameters=ntrip_params
      )
    ]
  )

  return launch.LaunchDescription([
    use_https_arg,
    host_arg,
    port_arg,
    mountpoint_arg,
    username_arg,
    password_arg,
    container1
  ])

