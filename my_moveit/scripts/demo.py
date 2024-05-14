#! /usr/bin/python3
import rospy
import moveit_msgs.msg
import copy
from std_msgs.msg import String
import moveit_commander
from moveit_commander.conversions import pose_to_list
import geometry_msgs.msg
from math import pi, tau, dist, fabs, cos
rospy.init_node("move_group_python_interface_tutorial", anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher(
    "/move_group/display_planned_path",
    moveit_msgs.msg.DisplayTrajectory,
    queue_size=20,
)
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "gripperBase"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.y = 0.1  
box_name = "box"
grasping_group = "hand"
touch_links = robot.get_link_names(group=grasping_group)


import math
def goStateOne():
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = math.radians(-75)
    joint_goal[2] = math.radians(80)
    joint_goal[3] = 0
    joint_goal[4] = math.radians(80)
    joint_goal[5] = 0  
    move_group.go(joint_goal, wait=True)
    move_group.stop()

def grabBox():
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "gripperBase"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.y = 0.1  
    box_name = "box"
    scene.add_box(box_name, box_pose, size=(0.075, 0.075, 0.075))
    grasping_group = "hand"
    touch_links = robot.get_link_names(group=grasping_group)
    eef_link = move_group.get_end_effector_link()
    scene.attach_box(eef_link, box_name, touch_links=touch_links)

def goStateTwo():
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = math.radians(-180)
    joint_goal[1] = math.radians(0)
    joint_goal[2] = math.radians(0)
    joint_goal[3] = 0
    joint_goal[4] = math.radians(80)
    joint_goal[5] = 0  
    move_group.go(joint_goal, wait=True)
    move_group.stop()
eef_link = move_group.get_end_effector_link()
def dropBox():
    scene.remove_attached_object(eef_link, name=box_name)
    scene.remove_world_object(box_name)




import time

for i in range(10):
    goStateOne()
    time.sleep(1)
    grabBox()
    time.sleep(1)
    goStateTwo()
    time.sleep(1)
    dropBox()
    time.sleep(1)
'''
waypoints = []
scale = 1
wpose = move_group.get_current_pose().pose
wposeOrig = copy.deepcopy(wpose)
wpose.position.z -= scale * 0.1  # First move up (z)
wpose.position.y += scale * 0.2  # and sideways (y)
waypoints.append(copy.deepcopy(wpose))

wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
waypoints.append(copy.deepcopy(wpose))

wpose.position.y -= scale * 0.1  # Third move sideways (y)
waypoints.append(copy.deepcopy(wpose))

waypoints2 = [wpose]
wpose.position.z += scale * 0.2
wpose.position.y += scale * 0.2
waypoints2.append(copy.deepcopy(wpose))
waypoints2.append(wposeOrig)

# We want the Cartesian path to be interpolated at a resolution of 1 cm
# which is why we will specify 0.01 as the eef_step in Cartesian
# translation.  We will disable the jump threshold by setting it to 0.0,
# ignoring the check for infeasible jumps in joint space, which is sufficient
# for this tutorial.
(plan, fraction) = move_group.compute_cartesian_path(
    waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
)  # jump_threshold

move_group.execute(plan, wait=True)
move_group.stop()
print("Part 1 done")
import time
time.sleep(1)
print("Starting part 2")
(plan, fraction) = move_group.compute_cartesian_path(
    waypoints2, 0.01, 0.0  # waypoints to follow  # eef_step
)  # jump_threshold

move_group.execute(plan, wait=True)
move_group.stop()
'''