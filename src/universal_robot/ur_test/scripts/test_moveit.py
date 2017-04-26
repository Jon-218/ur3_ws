#!/usr/bin/env python
import sys
import copy
import rospy
sys.path.append("/opt/ros/indigo/lib/python2.7/dist-packages/moveit_commander")
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

print "===================== Starting tutotial setup"
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',anonymous=True)
robot = moveit_commander.RobotCommander()
scence = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory)
print "===================== Waiting for Rviz..."
rospy.sleep(10)
print "===================== Starting tutorial "

print "===================== Reference frame: %s" % group.get_planning_frame()
print "===================== Reference frame: %s" % group.get_end_effector_link()
print "===================== Robot Groups:"
print robot.get_group_names()
print "===================== Print robot state"
print robot.get_current_state()
print "====================="

print "===================== Generating plan 1"
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1
pose_target.orientation.x = 0
pose_target.orientation.y = 0
pose_target.orientation.z = 0
pose_target.position.x = 0.29516
pose_target.position.y = 0.11232
pose_target.position.z = 0.37264
group.set_pose_target(pose_target)

plan1 = group.plan()
robot.move()
print "==================== Waiting while Rviz display plan1..."
rospy.sleep(5)
print "==================== Visualizing plan1"
display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
moveit_msgs.msg.DisplayTrajectory()
display_trajectory.append(plan1)
display_trajectory_publisher.publish(display_trajectory)

print "==================== Waiting while plan1 is visualized (again)..."
rospy.sleep(5)

moveit_commander.roscpp_shutdown()
