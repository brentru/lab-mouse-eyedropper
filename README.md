**Lab Mouse Eyedropper**
*Senior Capstone Design Project, UMassD 2018*

This repository contains an open-source (MIT License) control panel for a instrument to administer eyedrops to laboratory mice.

**NOTE**: this project is in-progress. it is not advised to use this on hardware yet, it's still buggy and in-development.

* Suggested Hardware Stack:
	* Modified Marlin Firmware (Lab-Mouse-Eyedropper-Firmware)
	* RAMPS 1.4 + drv8825 stepper driver (x5)
	* Arduino MEGA (atmega 2650)


**Installation**

First, **install PyQt5** from [source](https://riverbankcomputing.com/software/pyqt/download5) 

Then, make sure you're running python3/pip3 and **install the following required dependencies: PySerial, OpenCV**

OpenCV Installation:

    pip install matplotlib
    pip install numpy
    pip install opencv-python

pySerial Installation:

     pip install pyserial


*note*: the following instructions take place within `/lab-mouse-eyedropper/app`


**Build the UI (macOS/Unix):**
run `python setup.py build_ui`
then, run `pip install -e .`

**Build the UI (Windows):**
run `$ pyuic5 -x posiapp/gui/mainwindow.ui -o posiapp/gui/mainwindow_ui.py`
then, run `pip install -e .`

**Launch the  application:**
run: `python -m posiapp`
