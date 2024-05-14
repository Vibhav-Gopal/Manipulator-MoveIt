# Sample Pick and Place manipulator simulation
---
## How to run it and visualise it?
Follow below instructions to start visualising  
Assumptions: 
- ROS and Dependencies are installed

Commands:
```
mkdir ~/my_ws/src && cd ~/my_ws
git clone https://github.com/Vibhav-Gopal/Manipulator-MoveIt.git src
catkin_make && source devel/setup.bash
```
The above commands will clone the repo and set the environment up.
Now lets start the RViz visualisation
```
roslaunch my_moveit demo.launch
```
This will open up RViz window and start the MotionPlanning framework  

Now lets run the demo sequence of pick and place
```
rosrun my_moveit demo.py
```
We can see the manipulator move to a specific location, then a box appears, which is the attached to the manipulator and the manipulator carries the box to another location where it is detached after which the box is deleted from the scene.
This keeps repeating 10 times after which it stops moving.  
To play around with this model and have full control over the joints run the following command
```
roslaunch urdf_tutorial display.launch model:=<path to model>
```
The model is provided in URDF format in the `proper_test` package and can be utilised.

## What's running under the hood?
This manipulator is developed using the MoveIt framwork. The model of the manipulator is taken from **Universal Robotics UR3e** model available on their website.  
The model has been taken in `*.step`, using **FreeCAD** each of the links are exported separately into `*.dae` format where they were then imported into **Blender** and the origins of the models were corrected.  
Then the model has been assembled using the knowledge of the position of origins via a `.urdf` file, written by me, found in the `proper_test` package.  
The `.urdf` file is then fed into **MoveIt Setup Assistant** which helps integrate the model with **MoveIt**. Using MoveIt's python interface, I was able to control the manipulator programatically.

## So what's the other simulator?
I used URSim -E edition, which is the official programming interface for UR Cobots, I launched the VM using **VMWare** then created a new program for **UR3 Series** Cobots, the detailed filepaths will be available in the 
README file placed on the desktop. A zip archive of the VM is provided [here](https://drive.google.com/file/d/1g6D013-BWzzRiY8WmaCXop6lHv1ZENwb/view?usp=sharing).

## Time taken and Challenges :
- Time Taken : Approx. 18 Hours (Spread over 3 days)
- Main Challenges faced
  - Knew about URDF mainly in theory, learning it via practice
  - Figuring out how to assemble the robot in URDF
  - Setting up MoveIt Package
  - Issues with drivers and software

As seen, most of the challenges were very basic ones, and there were no significant obstacles in the development of this repo. The **URSim** GUI was also fairly straightforward, and so was the **MoveIt Setup Assistant**. Knowing why you are doing what you are doing is very important. I believe I've understood everything I've done, down to the last semicolon.
With the newfound experience, faster iteration is now possible for similar problem statements.

