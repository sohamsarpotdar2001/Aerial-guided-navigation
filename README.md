# Aerial-guided-navigation

This project implements an autonomous navigation system where a TurtleBot robot is guided by a quadcopter. The quadcopter creates and updates a global 3D map of the environment using a depth camera, and sends navigation commands to the TurtleBot in real-time. This system was developed using ROS and simulated in Gazebo. After successful simulations, hardware tests were conducted with a custom-built Px4 quadcopter and TurtleBot robot.

## Features
- **Aerial 3D Mapping**: The quadcopter uses a depth camera to create a 3D map of the environment from an aerial perspective.
- **Guided Navigation**: The TurtleBot receives navigation commands from the quadcopter, enabling it to autonomously move within the mapped environment.
- **Real-time Updates**: The quadcopter continuously updates the global map, ensuring the TurtleBot has up-to-date navigation data.
- **ROS & Gazebo Integration**: The entire simulation was developed in ROS and tested in the Gazebo environment before transitioning to real hardware.

## Project Workflow
1. **Simulations**: 
   - Developed and tested in **Gazebo** using **ROS** for both the TurtleBot and quadcopter.
   - Simulated aerial mapping and TurtleBot navigation within the environment.

2. **Hardware Implementation**: 
   - Built a custom **Px4 quadcopter** equipped with a **depth camera** to create the 3D environment map.
   - Deployed the TurtleBot robot on the ground to navigate based on commands from the quadcopter.
   - The quadcopter communicated real-time navigation commands to the TurtleBot for autonomous movement.

## Installation and Setup
### Prerequisites
- **ROS** (tested on ROS Noetic)
- **Gazebo** (tested on Gazebo 11)
- **TurtleBot** (ROS TurtleBot packages)
- **Depth Camera** (compatible with ROS)

### Steps
1. Install ROS Noetic, [PX4 Firmware](https://github.com/PX4/PX4-Autopilot) and [rtabmap](https://github.com/introlab/rtabmap_ros) package:
    ```bash
    sudo apt install ros-noetic-turtlebot3 ros-noetic-mavros ros-noetic-depthimage-to-laserscan
    ```

2. Clone the project repository:
    ```bash
    https://github.com/sohamsarpotdar2001/Aerial-guided-navigation.git
    cd Aerial-guided-navigation
    ```

3. Run the simulation in Gazebo:
    ```bash
    roslaunch drone_and_turtlebot.launch
    roslaunch mapping.launch
    roslaunch mapping_rviz.launch
    ```

## Working
- **Mapping**: The quadcopter flies over the environment and uses its depth camera to create a 3D map of the surroundings.
- **Command Transmission**: The quadcopter analyzes the map and computes the best navigation commands for the TurtleBot.
- **Navigation**: The TurtleBot receives the commands and autonomously moves within the environment, avoiding obstacles and navigating efficiently.

## Hardware Setup
- **Quadcopter**: Custom-built quadcopter running Px4 firmware.
  - **Sensors**: Depth camera for mapping.
- **TurtleBot**: Ground robot controlled via ROS.
  - **Communication**: Receives navigation commands from the quadcopter through ROS topics.

## Simulation Environment
- **Gazebo**: Simulated the environment with obstacles and varying terrain.
- **ROS**: Managed communication between the quadcopter and TurtleBot.

## Future Improvements
- **SLAM Integration**: Incorporate SLAM algorithms for more robust localization.
- **Multi-UAV System**: Expand the system to work with multiple UAVs collaborating to guide multiple robots.
