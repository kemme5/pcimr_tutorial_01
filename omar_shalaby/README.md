# Practical Course: Intelligent Mobile Robots with ROS (PCIMR)




# Tutorial 2:
##### Omar Shalaby: 
###### ga53laj@mytum.de kemya1995@gmail.com

In order to startup the simulation environment first export the required robot [either p3dx (pioneer) or rto-1 (robotino)] :

```
  $ export ROBOT = p3dx 
```

or

```
  $ export ROBOT = rto-1
```


Upon choosing the required robot then launch the simuation in Gazebo by running :

```
  $ roslaunch rto_bringup_sim robot.launch
```
Then you need to set the 3 rosparameters ***robot_name*** (1 for Pioneer, 0 for Robotino ***Default in launch file = 0***) that sets the correct topic name, ***max_velocity*** (***Default in launch file = 1.0***) the required max velocity in any axis and ***min_dist*** (***Default in launch file = 0.35***) the min required safe distance to obstacles. Do that by entering :

```
  $ rosparam set /rob_name 0
  $ rosparam set /max_velocity 1.0
  $ rosparam set /min_dist 0.35
```

You can now launch the teleop node to control using the keyboard ***NOTE: You have to specify the teleop topic when launching by running:***

```
  $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=teleop_cmd_vel
```

Now run the control node itself using :

```
  $ rosrun pcimr_omar_tutorial1 tutorial2_controller
```

You can also a launch file directly with all the parameters and the node by running:

```
  $ roslaunch pcimr_omar_tutorial1 tut2.launch 
```

So all is working fine for me, im just having trouble dealing with backing up or blind angles, should i've sampled the entire range rather than only a couple of angles ??



