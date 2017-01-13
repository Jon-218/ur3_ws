#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String

def move_group_python_interface_tutorial():
    print "========== Starting tutorial setup"
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("manipulator")
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

    print "==========Waiting for rviz.."
    rospy.sleep(3)
    print "==========Starting tutorial"

    print "========== Reference frame: %s" % group.get_planning_frame()

    print "========== Reference frame: %s" % group.get_end_effector_link()
    print "========== Robot Groups:"
    print robot.get_group_names()

    print "========== print robot state"
    print robot.get_current_state()
    print "============================"


    taret_pose1 = geometry_msgs.msg.Pose()
    taret_pose1.position.x = 0.4218
    taret_pose1.position.y = 0.1942
    taret_pose1.position.z = 0.0965
    taret_pose1.orientation.x = -0.211307
    taret_pose1.orientation.y = 0.467779
    taret_pose1.orientation.z = 0.640848
    taret_pose1.orientation.w = 0.570828
    group.set_pose_target(taret_pose1)

    plan1 = group.plan()
    print "============= Wainting while rviz display plan1..."
    rospy.sleep(2)

if __name__=='__main__':
    try:
        move_group_python_interface_tutorial()
    except rospy.ROSInterruptException:
        pass
