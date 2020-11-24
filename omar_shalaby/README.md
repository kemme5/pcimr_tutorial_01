# Practical Course: Intelligent Mobile Robots with ROS (PCIMR)




# Tutorial 2:
##### Omar Shalaby: 
###### ga53laj@mytum.de kemya1995@gmail.com

  - Note: For some reason while developing i could not get the sensor to give me any values whatsoever [always -inf i tried doing everything i could but still. Also the name space for the pioneer was /pioneer rathar than that given in the tutorial description, since i coded what i understood without having any sensor data let's hope the approach is at least correct]

  


IDEA:
 - The differential robot should check if the obstacle is right infront of it while moving (there's no other moving option) implement this decaying velocity until it stops

 - For the omnidirectional one, since motion can be anywhere, my idea was to resolve the given velocity command to get the RESULTANT ANGLE of the velocity and given this angle, relative to the robot ofcourse, do the same decaying algo this was my first try, then i though it would be easier to find the min distance to an obstacle and limit motion towards it, again development was almost impossible without a sensor, pls advise me what i did wrong :)

### Running The Code


##### Nodes
- To run the controller (make sure the name space is correct)
```
 $ rosrun rosrun pcimr_omar_tutorial1 tutorial2_controller.py
```
-Unfortunately wasnt able to do the launch file since i was struggling with the sensor

