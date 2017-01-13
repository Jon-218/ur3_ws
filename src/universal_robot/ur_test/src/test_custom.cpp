#include <iostream>
#include <moveit/move_group_interface/move_group.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>
#include <moveit/kinematic_constraints/utils.h>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "test_custom_node");
	ros::NodeHandle node_handle;
	ros::AsyncSpinner spinner(1);
	spinner.start();
	moveit::planning_interface::MoveGroup group("manipulator");
	moveit::planning_interface::PlanningSceneInterface planning_scene_interface;
	ros::Publisher display_publisher = node_handle.advertise<moveit_msgs::DisplayTrajectory>("/move_group/display_planned_path", 1, true);
	moveit_msgs::DisplayTrajectory display_trajectory;

	std::cout<<"DefualtPlannerID: "<<group.getDefaultPlannerId("manipulator")<<std::endl;

	geometry_msgs::Pose target_pose1;
	target_pose1.position.x = 0.4218;
	target_pose1.position.y = 0.1942;
	target_pose1.position.z = 0.0965;
	target_pose1.orientation.x = -0.211307;
	target_pose1.orientation.y = 0.467779;
	target_pose1.orientation.z = 0.640848;
	target_pose1.orientation.w = 0.570828;
	group.setPoseTarget(target_pose1);

	geometry_msgs::Pose target_pose0 = target_pose1;
	geometry_msgs::Pose target_pose2 = target_pose1;
	target_pose0.position.z += 0.1;
	target_pose2.position.x -= 0.2;

	geometry_msgs::PoseStamped pose;
	pose.header.frame_id = "base_link";
	pose.pose = target_pose0;
	std::vector<double> tolerance_pose(3, 0.01);
	std::vector<double> tolerance_angle(3, 0.01);

	moveit_msgs::Constraints pose_constraints = kinematic_constraints::constructGoalConstraints("ee_link", pose, tolerance_pose, tolerance_angle);
//	group.setPathConstraints(pose_constraints);
//	moveit::planning_interface::MoveGroup::Plan my_plan;
	bool success = group.move();

	group.clearPathConstraints();
//	group.setPoseTarget(target_pose2);
//	sleep(1);
//	bool success2 = group.move();

	ROS_INFO("Visuallizing plan 1 (pose goal) %s", success?"":"FAILED");
//	ROS_INFO("Visuallizing plan 2 (pose goal) %s", success2?"":"FAILED");
//	ROS_INFO("Visuallizing execute 1 (pose goal) %s", success2?"":"FAILED");

	sleep(1.0);
	ros::shutdown();
	return 0;
}
