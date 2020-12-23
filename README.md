# Practical Course: Intelligent Mobile Robots with ROS (PCIMR)

## Tutorial 03: Probability Theory & Localization

### Introduction

##### Omar Shalaby Tutorial 3

The purpose of this tutorial is to demonstrate basic knowledge of probability theory as well as an understanding of the principles of mobile robot localization. You can solve this task using either C++ or Python.

After completing this exercise you should be able to
- understand work with uncertainties in robotics and beyond
- understand how mobile robot localization works in general, including the challenges that arise:
  - potential problems due to uncertainties in the sensor, movement, etc.
  - discretization/approximation of the real-world
- implement a variety of mobile robot localization algorithms

If you have trouble understanding the code or writing your own, please have a look at the [tutorials](http://wiki.ros.org/ROS/Tutorials) again.



---
### Code Overview


Visit the provided github [repository]() and have a look at the code for this exercise by checking out the branch *tutorial-03*. You fill find the same simulator used in the first exercise but with a few modifications. The world that we will be using for this exercise is shown in Fig. 1.

As a reminder, the simulation can be started by


   $ rosrun pcimr_simulation simple_sim_node
   


Instead of the robots position, the simulator now publishes the map, as you will need it for localizing the robot in the environment. Besides that, the simulation node is still publishing the sensor data (*/scan*) with 4 range measurements by default, see Fig. 2. 

The node also still subscribes to the */move* topic, but you don’t have to send any commands this time. This task is performed by the *navigator_node*, located in the new pcimr_navigation package. 


### Tutorial

I wanted to thank you guys one more time for the extension, it was a pretty hard month and i barely did anything while dealing with my personal problems.

Would like to also acknowledge getting help from a couple of friends and team members since that one was pretty difficult for me

In essence i went with running everything in subroutines called whenever a subscribed message is received (As pointed out by robin in a rocketchat reply) and the entire algorithm carries from there, was also introduced to some pretty cool list functions since i mainly used loops but that one was an eye opener.

To run the localization node :



 $ rosrun pcimr_localization localization_node 



The simulation and navigation nodes should be also up and running first by using :



 $ roslaunch pcimr_navigation navigation.launch




Still a bit buggy trying to put final touches 
Changing the inital probabilities didnt affect it that badly...
The kidnapped robot problem just made the robot take longer at the beginning, specially if the new position is kind of far away
