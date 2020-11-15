# Practical Course: Intelligent Mobile Robots with ROS (PCIMR)




# Tutorial 1:
##### Omar Shalaby: 
###### ga53laj@mytum.de kemya1995@gmail.com

  - Note: I had to change the schebang operator to 
```py
 #!/usr/bin/env python3
```

  


Information Given:
  - The goal [as shown by red square on map] is at location (16, 12)
  - This can be described as keep moving North (N) till you encounter an obtacle then move East (E) till an obstacle then (N) then finally (E)
  - Since the goal is static this can also be transformed into steps which are : 11 (N), 11 (E), 1 (N), 3 (E)

>The simple_robot_node didnt have any published message regarding the goal  position or any [Info] msg returning success in that case the goal is assumed to be always at location (X, Y) = (16, 12)




Two python nodes were implemented in this tutorial.

The First Node simply goes to the goal at 16,12 by following the simple guide, keep moving North till you find the wall then move east, north and east again till you find the goal.

The Second Node takes a goal location as an argument and tries to reach it though naive maze solving.

### Running The Code

Just a quick reminder, again i guess i had an env issue and had to alter the schebang to i guess for my code to work on your env change from python3 to python:

```py
 #!/usr/bin/env python3
```
To run the code first make sure ROS Master is running together with the simulator node by running
```py
 $ rosrun pcimr_simulation simple_sim_node
```
##### Nodes
- To run the simple logical node [known path]
```py
 $ rosrun rosrun pcimr_omar_tutorial1 simple_logic_node.py
```

- To run the naive Maze Solver
```py
 $ rosrun rosrun pcimr_omar_tutorial1 naive_maze.py
```






