# Robot Vision
To get this to work you must also download and or start a [ip camera](https://github.com/mishiki1002/Ip_Camera) with what ever device you. I will be using a [raspberry pi](https://www.raspberrypi.org/) for this example.

## Set up
The very first thing you need to do is to flash the [Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/) image to a sd card. Then insert it to the raspberry pi. Then you need to connect the raspberry pi camera and boot up with a monitor or shh. After that you need to then enable raspicamera access. To do this you need to type in the console ```sudo raspi-config``` Afther you do that you will get a screen similar to this

![Raspi-Config-Screenshot](http://jeelabs.org/wp-content/uploads/2013/06/Screen-Shot-2013-05-28-at-16.52.58.png)


After that you need to click enable camera. It will then ask you to reboot, agree and then wait for it boot up. Now that we have enabled the camera we can install vlc for raspberry pi by using ```sudo apt install vlc```. After that is done you want to clone the ip camera repsoitory to your home file system ```git clone https://github.com/mishiki1002/Ip_Camera.git```, after it is completed you enter the directory and use this command for execution ```make ip```. now you have succesfully created your own ip camera on a raspberry pi. Next you need to get the ip of the raspberry pi and replace the 0 in ```line 15``` in ```main.py``` with your pi's ip address


## Screenshots
![promo photo one](screenshots/promo_photo1.png)

### Resources
 - http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
 - https://github.com/Team2168/2168_Vision_Example
 - https://github.com/wpilibsuite/opencv

