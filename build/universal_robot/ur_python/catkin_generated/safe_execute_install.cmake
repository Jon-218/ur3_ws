execute_process(COMMAND "/home/jon/ros/indigo/ur3_ws/build/universal_robot/ur_python/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jon/ros/indigo/ur3_ws/build/universal_robot/ur_python/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
