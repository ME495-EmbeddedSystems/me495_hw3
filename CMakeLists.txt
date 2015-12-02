cmake_minimum_required(VERSION 2.8.3)
project(me495_hw3)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  tf
  turtlesim
  teleop_twist_joy
  message_generation
  )

add_service_files(
  FILES
  WallMeasurement.srv
  )

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package()
