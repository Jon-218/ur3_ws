cmake_minimum_required(VERSION 2.8.3)
project(ur_test)
include(/usr/share/cmake-2.8/Modules/FindCUDA.cmake)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cmake_modules
  interactive_markers
  moveit_core
  moveit_ros_perception
  moveit_ros_planning_interface
  pluginlib
  roscpp
	rospy
  std_msgs
)

#catkin_python_setup()

#install(PROGRAMS script/test_moveit.py
	#DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ur_test
#  CATKIN_DEPENDS cmake_modules interactive_markers moveit_core moveit_ros_perception moveit_ros_planning_interface pluginlib roscpp std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(test_random_node src/test_random.cpp)

add_dependencies(test_random_node ur_test_generate_messages_cpp)

target_link_libraries(test_random_node
	${catkin_LIBRARIES}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(test_custom_node src/test_custom.cpp)

add_dependencies(test_custom_node ur_test_generate_messages_cpp)

target_link_libraries(test_custom_node
	${catkin_LIBRARIES}
)

## Declare a cpp executable
add_executable(test_home_node src/test_home.cpp)

add_dependencies(test_home_node ur_test_generate_messages_cpp)

target_link_libraries(test_home_node
	${catkin_LIBRARIES}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(test_joint_node src/test_joint.cpp)

add_dependencies(test_joint_node ur_test_generate_messages_cpp)

target_link_libraries(test_joint_node
	${catkin_LIBRARIES}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(test_kinematic_node src/test_kinematic.cpp)

add_dependencies(test_kinematic_node ur_test_generate_messages_cpp)

target_link_libraries(test_kinematic_node
	${catkin_LIBRARIES}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(add_collision_node src/add_collision.cpp)

add_dependencies(add_collision_node ur_test_generate_messages_cpp)

target_link_libraries(add_collision_node
	${catkin_LIBRARIES}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(test_collision_node src/test_collision.cpp)

add_dependencies(test_collision_node ur_test_generate_messages_cpp)

target_link_libraries(test_collision_node
	${catkin_LIBRARIES}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp executable
add_executable(test_tcp_node src/test_tcp.cpp)

add_dependencies(test_tcp_node ur_test_generate_messages_cpp)

target_link_libraries(test_tcp_node
	${catkin_LIBRARIES}
)

## Declare a cpp executable
add_executable(test_cli_node src/test_client.cpp)

add_dependencies(test_cli_node ur_test_generate_messages_cpp)

target_link_libraries(test_cli_node
	${catkin_LIBRARIES}
)

## Declare a cpp executable
#ADD_EXECUTABLE(TEST_CUDA_NODE SRC/TEST_CUDA.CPP)
#cuda_add_executable(test_cuda_node 
	#src/test_cuda.cpp 
	#src/cuda.cu)

#add_dependencies(test_cuda_node ur_test_generate_messages_cpp)

#target_link_libraries(test_cuda_node
	#${catkin_LIBRARIES}
#)

## Declare a cpp executable
add_executable(test_scene_node src/test_scene.cpp)

add_dependencies(test_scene_node ur_test_generate_messages_cpp)

target_link_libraries(test_scene_node
	${catkin_LIBRARIES}
)
