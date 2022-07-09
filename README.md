# This is our code specially made for the SFHMMY 2021 Workshop.

Presenters: Sotiris Barlakas - Minas Kosmidis

Theme: An introduction to ROS with a simulation of autonomous obstacle avoidance in GAZEBO simulator.

Description: A differential drive robot model is created in URDF format, in order to be simulated in GAZEBO Simulator. We then create simple Publisher and Subscriber
nodes in ROS to make the robot avoid obstacles autonomously in an unknown map.
More specifically, the Subscriber receives info from the lidar that we added to our model. 
The publisher proceeds this information and decides the desired actuator movement
which is sent (published) to the robot's simulated actuators
