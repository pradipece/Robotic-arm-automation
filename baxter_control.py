# Import the necessary modules of python
import rospy
import baxter_interface 

from baxter_interface import CHECK_VERSION
# initialize our ROS node
rospy.init_node('project_5')
print("Getting robot state...")
r = baxter_interface.RobotEnable(CHECK_VERSION)
init = r.state().enabled.   #Robot enabled 
print("Enabling robot before start to pick and place...")
r.enable()
rt = baxter_interface.Limb('right')
# get the right and left limb's current joint angles
por = rt.joint_angles()
rightgripper = baxter_interface.Gripper('right')
lt = baxter_interface.Limb('left')
leftgripper = baxter_interface.Gripper('left')
