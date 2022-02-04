
<div align="center">
  
![ros4](https://user-images.githubusercontent.com/78342516/152425168-dfcc35bf-6dd3-445f-a1cd-bf0d3f41a566.jpeg)


  <h1 align="center">Multipurpose Household Bot</h1>

  <p align="center">
    One bot that does it all!
    <br />
    <a href=" "><strong>Explore the demo here »</strong></a>
    <br />
    <br />
    <a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/issues">Request Feature</a>
  </p>
</div>



## Table of contents
<details>
  <ol>
    <li>
       <a href="#idea-behind-the-project">Idea Behind The Project</a>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#navigation">Navigation</a></li>
    <li><a href="#hardware">Hardware</a></li>
    <li>
      <a href="#features">Features</a>
      <ul>
        <li><a href="#face-detection">Face Detection</a></li>
        <li><a href="#baby-threat-detection">Baby Threat Detection</a></li>
        <li><a href="#baby-following">Baby Following</a></li></li>
    </ul>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Idea behind the project

The basic idea of this bot is to create a multi-purpose household bot with a lot of features which justifies its price for an average household. Most household bots today only do single things like cleaning, playing but without increasing hardware significantly (which will not increase the cost) we can add a lot of features. The bot will help in all day to day activities ranging from baby care, cleaning, security and a lot more. Many small and innovative ideas like detachable components and DIY tutorials will increase its usability and decrease cost. We will also make it modifiable and programmable by users so that they can experiment with it, learn, and add new features. 
The core idea is to  add innovative features with a limited hardware which solve small day to day problems.

This a boon for all the working parents out there who are looking for a reliable solution to their process of setting up a balance between parenting and work. We know how a parent wants the best for their child and is ready to spend any amount of money to establish an amazing future for them, but here, with our bot, we provide them with all the necessary help in the best quality while taking care of their pockets!

<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>

## About the project
We built our own vacuum cleaning household bot entirely from scratch using SolidWork and did various testing like airflow simulation,stress analysis guaranteeing its functionality in the real world. For navigation we used differential drive along with ROS Navigation stack and implemented 3 algorithms for Autonomus Mapping,Autonomus Navigation and Autonomus Optimal Complete Coverage.Also we implemented Resnet and YoloV3 Algorithms for Baby Monitoring.Threat Detection and Face Recognition.
### Built With

The technologies used while building and testing the project are:

* [ROS](https://www.ros.org/)
* [Gazebo](http://gazebosim.org/)
* [SolidWorks](https://www.solidworks.com/)


<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>
<!-- GETTING STARTED -->

## Getting Started

How to set-up the project

### Prerequisites

Before getting started, make sure your systme meets the following requirements:

* [ROS](https://www.ros.org/)
* [Gazebo](http://gazebosim.org/)
 
  

### Installation

Now that you're ready with the prerequisites, setup the project using the following steps-

```
cd catkin_ws/src
git clone https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot
catkin build ./
```
<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>

## Hardware

<p float="left">
  
 ![EXPLO (1)](https://user-images.githubusercontent.com/78342516/152426551-8dad213e-0cb0-48df-8a62-15b817a533c4.png)
 ![Copy of EXPLO](https://user-images.githubusercontent.com/78342516/152428330-dc7b0d41-897d-43df-a612-23594eee16fc.png)
![Copy of EXPLO (1)](https://user-images.githubusercontent.com/78342516/152428359-8a34a2b1-3949-44f9-a6a1-315e1bffa312.png)
  
</p>



The CAD model of the bot was created using Solidworks. Further, an URDF file was created using the model considering the motion along all the links which were to be controlled and simulated using ROS.The bot’s vacuum system is based on a centrifugal pump. Centrifugal pump is a machine that imparts energy to fluid .This energy can cause a fluid to flow or rise to a higher level. It consists of two basic parts: The rotary element or impeller and the stationary element or casing
The vacuum system of the bot sucks in air along with dust particles from the bottom and transports it to the detachable dust collector.The analysis of the vacuum system was done using the SolidWorks Flow Simulation tool. For Various parameters like air velocity, pressure and temperature were simulated and plots were obtained and various testing like airflow simulation,stress analysis was done guaranteeing its functionality in the real world


<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>


## Navigation

<img width="638" alt="ros" src="https://user-images.githubusercontent.com/78342516/152424295-a60876e4-98ac-4be3-befd-8f7058902725.PNG">


We used Differntial Drive along with ROS Navigation Stack on our Bot to autonomously navigate it through house.We developed 4 moods fot it's navigation-

 a.*Teleop Controlled*-In this ypu can simply control bots motion by publishing on cmd_vel topic.

 b.*Autonomus Mapping*This will be used when a new bot comes to home,in this bot will atonomusly map the whole house by finding regions which are not mapped.We used <a href="http://wiki.ros.org/explore_lite">explore_lite</a> along with ROS Navigation Stack for this.To launch this mood run
 ```bash
 roslaunch rbot mapping.launch
 ```
 
 c.*Autonmous Navigation*-This will allow you to autonomusly send bot anywhere in generated also avoiding both static and dynamic obstacles.We used ROS Navigation Stack along with <a href="http://wiki.ros.org/teb_local_planner">teb_local_planner</a> as local planner.To launch this mood run 
  ```bash
 roslaunch rbot navigation.launch
 ```
 d.*Autonomus Complete Coverage*-In night you can simply run this mood and bot will autonomusly vacuum your whole house following an optimal complete coverage path.We have used <a href="http://wiki.ros.org/full_coverage_path_planner">full_coverage_path_planner</a> as global planner along with teb_local_planner as local planner.To launch this mood run-
 ```bash
 roslaunch rbot complete_coverage.launch
 ```
  
Find the demo of Navigation implementation [here](https://drive.google.com/file/d/1GFb-_O2ioxu-zdwylFPfyHNaHDGUox7V/view)

<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>

## Features

### Face Recognition

- We use a custom build AI model, combinind both, a pretrained ResNet model and the OpenCV haarcascade funtion to develop face recognition algorithm.

- The weights of the model were pretrained, they convert the image into a vector of length 128. And then the vectors are compared between themselves using a siamese network architecture. 

- The OpenCV haarcascade function first detects all the images in a given frame and then compares the faces with those present in the database. (Already stored in the system)

- If the faces match or are within a threshold value, the bot recognises the person and greets him/ Her. If not, the bot considers it as an intruder and triggers an alarm through the system.
- You can see the code [here](https://colab.research.google.com/drive/1R8DMmd4irxbfXU8tUebgAP64VtLyI3eQ?usp=sharing)


<img width="638" alt="ros2" src="https://user-images.githubusercontent.com/78342516/152424555-22d898be-4785-43a8-8774-770f3140c19f.PNG">


Find the demo of Face Detection algorithm implementation [here](https://drive.google.com/file/d/1K6rV0f0d-TTYmIyUp-HNQ1cQ1N9isJMF/view)

### Baby Threat Detection

<img width="641" alt="ros3" src="https://user-images.githubusercontent.com/78342516/152424816-6c31d4d6-59c6-4d9f-8395-a29e82bfba5b.PNG">


Find the demo of Threat Detection for baby  [here](https://drive.google.com/file/d/1K5NE13m8MZG6SAx4-36VjofmkLH4Blgi/view)

### Baby Following

Find the demo of baby follwoing [here](https://drive.google.com/file/d/1JxuwaeDJQHta6C9UJmLCamdO-b6d8-8v/view)


<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
From cleaning the house to taking care of their baby by monitoring and following it, our bot is just what a working parent needs for their child. You can even video call from any remote location using our bot!
Communication, security, hygiene, child’s social growth, you name it and we’ve got it covered with our bot that is truly multipurpose.

The project is open source and you are free to modify as per your needs. 


<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Built our very own bot design completely from scratch
- [x] Testing of Airflow (CFD-Computational Fluid Dynamics)
- [x] Testing of Stress analysis (FEA-Finite Element Analysis)
- [x] Implemented custom-written YoLoV3  and ResNet algorithms
- [x] Created algorithms for navigation and complete-coverage vacuuming for the bot 
- [ ] Hardware of the bot (awaiting funding for our innovative idea)


See the [open issues](https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b branchName`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin  branchName`)
5. Open a Pull Request

<p align="right">(<a href="https://github.com/harshmahesheka/Multi-Purpose-HouseHold-Bot/blob/main/README.md">back to top</a>)</p>
