# Touchless Customer Feedback Device

## Description and Motivation
This is a computer vision software for a customer feedback device. The software uses Google's MediaPipe Hands artificial intelligence model API. It is meant to replace typical touch-based customer feedback devices like the one below.

<p align=center>
<img src="https://github.com/lbarnawi/Touchless_customer_feedback_survey_device_/blob/master/Typical%20customer%20feedback%20device.png?raw=true" alt="Typical customer feedback device" height=500px>
</p>

## Working Concept 

The device needs an input sensor (camera) and an output source (screen), the camera captures the hand within its field of view and then pass it to the MediaPipe Hand model-written using Python- for it to:
* 1- Detect hand
* 2- Find hand landmarks
* 3- Detect hand gesture

Next, a simple Graphical User Interface-written using Tkinter-is used to display the feedback of the user which could be one of three options: 
* Satisfied
* Unsatisfied
* Netural 

Moreover, these three feedback options could be tailored based on the user's needs. 


<p align=center>
<img src="https://github.com/lbarnawi/Touchless_customer_feedback_survey_device_/blob/master/working%20concept.png?raw=true" alt="Working concept" height=500px>
</p>



## Dependencies

The software uses external libraries which can be installed using the requirements.txt file.

While in the same project directory run:

```
pip install requirements.txt
```
Or
```
pip3 install requirements.txt
```

## Usage

To run the software, after installing above dependencies run the GUI.py or use ther terminal:
```
python gui.py
```
