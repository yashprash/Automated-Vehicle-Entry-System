# Automated Vehicle Entry System

## Technology Stack
Internet of Things (Raspberry Pi module, camera, ultrasonic sensor, Firebase, ThingSpeak), Image Processing (Python OpenCV, PyTesseract OCR)

## Introduction
This system is designed to provide automated access control to vehicles using a vehicle number plate character recognition process. First, the picture of the vehicle along with its number plate is captured using a camera connected to a Raspberry Pi module. The number plate is then identified from the rest of the picture using OpenCV. The text is then extracted and compared with the number plates of authorized vehicles. If the registration number matches, the vehicle is granted access to the authorized space (garage/ apartment/ toll). 

## Description
The Raspberry Pi camera is mounted on a Raspberry Pi3 board. Additionally, an ultrasonic sensor is connected to the Raspberry Pi. When the ultrasonic sensor (HC-SR04) detects an object in its proximity, an image is captured by the Raspberry Pi camera. The image captured will consist of a single frame large enough to accommodate the image of a portion of the car with the standard sized number plate. The image is then transferred to Google’s cloud-based platform Firebase using the Python library Pyrebase. Next, the image is retrieved from the Firebase storage by code running in a Google Colab notebook, in order to perform image processing using the number plate detection algorithm, implemented using OpenCV methods. First, gaussian blur is applied to reduce image noise and image detail, following which CVTColor is used to convert the image to grayscale. Sobel is then used to further smoothen the image. Furthermore, threshold is applied to change the colour of every pixel to either black or white. Rectangles are detected in the image, and the ratio of the rectangles sides’ and their area are checked to see if they are in a certain range, corresponding to that of standard number plate sizes. Then the ideal number-plate sized rectangle is obtained from the picture, in the form of a bounding box. Once the coordinates of the number plate are extracted, it is cropped and is passed through certain OpenCV methods proved to increase OCR accuracy. Lastly, PyTesseract is used to recognize the text in the cropped number plate image. Once the text is extracted, it is uploaded to ThingSpeak cloud, which is retrieved by the code running in the Raspberry Pi, and is then matched to the set of authorized number plates available. 

## Application
The system uses the approaches of image processing performed using Python, and Internet of Things implemented using a Raspberry Pi unit, to provide a practical approach for automated access control at security points in personal dwellings and apartments. 

### Test Image
![1](https://github.com/yashprash/yashprash.github.io/Automated-Vehicle-Entry-System/blob/gh-pages/1.jpg)

### Number Plate Recognized 
![2](https://raw.githubusercontent.com/yashprash/Automated-Vehicle-Entry-System/gh-pages/2.jpg)

### Number Plate Cropped to Perform OCR
![3](https://raw.githubusercontent.com/yashprash/Automated-Vehicle-Entry-System/gh-pages/3.jpg)

### Number Plate Characters Detected
![4](https://raw.githubusercontent.com/yashprash/Automated-Vehicle-Entry-System/gh-pages/4.png)

### Raspberry Pi Output
![5](https://raw.githubusercontent.com/yashprash/Automated-Vehicle-Entry-System/gh-pages/5.PNG)

### Raspberry Pi Setup with Camera, Ultrasonic Sensor and LED
![6](https://raw.githubusercontent.com/yashprash/Automated-Vehicle-Entry-System/gh-pages/6.JPG)
