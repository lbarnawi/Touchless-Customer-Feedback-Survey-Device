# Touchless Customer Feedback Device

### Discription and Motivation
This is a computer vision Software for a customer feedback device. The software uses Google's MediaPipe Hands artificiall intellegance model API. It is meant to replace typical touch-based customer feedback devices like the one below.

<p align=center>
<img src="https://github.com/JohannesAutenrieb/TeamACranfieldUAVSwarm/blob/master/img/Statemachine_main.png" alt="Statemachine_main" height=500px>
</p>

#### Working Concept 

The device needs an input sensor (camera) and an output source (screen), the camera captures the hand wtihing its field of view and then pass it to MediaPipe Hand model-written using Python- for it to:
* Detect hand
* Find hand landmarks
* Detect hand gesture
Next, a simple Graphical User Interface-written using Tkinter-is used to dispaly the feedback of the user which could be one of three options: 
* Satisfied
* Unsatisfied
* Netural 
Moreover, these three feedback options could be tailored based on the user needs. 




<p align=center>
<img src="https://github.com/JohannesAutenrieb/TeamACranfieldUAVSwarm/blob/master/img/Statemachine_main.png" alt="Statemachine_main" height=500px>
</p>



<p align=center>
<img src="https://github.com/JohannesAutenrieb/TeamACranfieldUAVSwarm/blob/master/img/System_Overview.png" alt="System_Overview" height=500px>
</p>




## Dependencies

The software uses external libraries which can be installed using the requirements.txt file.

Install Rospy for Pyton 3.6:

	sudo pip3 install -U rospkg
	sudo pip3 install roslibpy
	sudo apt-get install python3-yaml
	sudo pip3 install rospkg catkin_pkg

Install PyQt, PyUic4 and PyRcc4:

	sudo apt-get install pyqt4-dev-tools qt4-designer


**The software was tested under Linux Ubuntu Versions 16.04.6 LTS and 18.04.2 LTS*-** 

### Usage

This Software system is using ROS for that reason it needs to be integrated in a Robot Operating System Framework. If not allready existing, a working ROS Workspace needs to be created. If that is the case, please go first to your workspace.

	# Go to your ROS Workspace Directory
	$ cd ~/your_ros_workspace

Next Step is to clone this github repository and use it as a new package:

	$  git clone https://github.com/JohannesAutenrieb/mission_planning.git ./src/mission_planning

The system is build with:
	
	#Building all ROS packages
	$  catkin_make

To have a fucntional Task Allocation sytem the system needs inital agent information to start. When the sytem is not embedded in the completele ROS environment, the publisher.py can be used to fake the swarm:

	# fakes a swarm environment with 5 agents and 2 moving targets
	$  rosrun mission_planning publisher.py

The task allocation software is started with:
	
	$  rosrun mission_planning Main.py

The task manager software is started with:

	$  rosrun mission_planning TaskManager.py

When it is wanted to display the mission via the gui, the gui can started with:

	$  rosrun mission_planning GUI.py


License
-------

Released under the 2-clause GPL GNU license, see `LICENSE`.

Copyright (C) 2019, Johannes Autenrieb and Natalia Strawa