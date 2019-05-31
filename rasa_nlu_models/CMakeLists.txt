cmake_minimum_required(VERSION 2.8.3)
project(rasa_nlu_models)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslint
)

roslint_python()
catkin_python_setup()

catkin_package(
 CATKIN_DEPENDS
   rospy
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
