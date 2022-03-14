# Touchless Customer Feedback Device

## Description and Motivation
This is a computer vision software for a customer feedback device. The software uses Google's MediaPipe Hands artificial intelligence model API. It is meant to replace typical touch-based customer feedback devices like the one below.

<p align=center>
<img src="https://github.com/lbarnawi/Touchless_customer_feedback_survey_device_/blob/master/Typical%20customer%20feedback%20device.png?raw=true" alt="Typical customer feedback device" height=350>
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


<p align=center>
<img src="https://github.com/lbarnawi/Touchless_customer_feedback_survey_device_/blob/master/device%20GUI.gif" alt="Device GUI" height=350px><img src="https://github.com/lbarnawi/Touchless_customer_feedback_survey_device_/blob/master/MediaPipe%20Hand%20Model%20back-end%20process.gif?raw=true" alt="MediaPipe Hand model backend process" height=350>
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

## How to run the software?

To run the software, after installing above dependencies run the GUI.py or use ther terminal:
```
python gui.py
```
##### I tested the software on two platforms with the following performance:

* Acer laptop Intel( R) Core( TM) i 7 3537 U CPU @ 2.00 GHz 2.50 GHz) processor running Windows 11 using two different IDE's Pycharm and Visual Studio Code and the speed achieved was 20 FPS which is relatively slow.
* A quadcore Raspberry pi 4 (Broadcom BCM 2711 , Quad core Cortex A 72 ARM v 8 ) 64 bit SoC @ 1.5 GHz running Ubuntu Desktop 21.10, and the speed achieved was 12 FPS which is relatively slow.


#### Resources
* https://github.com/google/mediapipe
* https://www.youtube.com/watch?v=NZde8Xt78Iw&t=272s
* https://www.youtube.com/watch?v=p5Z_GGRCI5s&t=1847s
* https://www.youtube.com/watch?v=vQZ4IvB07ec&t=534s
