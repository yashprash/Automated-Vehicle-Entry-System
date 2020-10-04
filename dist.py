import RPi.GPIO as GPIO
import time
import signal
import sys
import picamera
import pyrebase
import urllib
import json

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "serviceAccount": ""
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# use Raspberry Pi board pin numbers

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# set GPIO Pins
pinTrigger = 18
pinEcho = 24
#camera=picamera.PiCamera()

def on_servo():
        print("Access Granted")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(14,GPIO.OUT)
        GPIO.output(14,GPIO.HIGH)
        time.sleep(10)
        GPIO.output(14,GPIO.LOW)

numbers=['DL3CAY9324','KA05JN8329']
def retrieve():
        print("Processing Image")
        time.sleep(2)
        print("Retrieving Number plate")
        time.sleep(2)
        baseURL='https://api.thingspeak.com/channels/654519/fields/1.json?api_key='
        f = urllib.request.urlopen(baseURL)
        response = f.read()
        data=json.loads(response.decode('utf-8'))
        number_plate=data['feeds'][1]['field1']
        print(number_plate)
        f.close()
        if number_plate in numbers:
                on_servo()

def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


while 1:
    # set Trigger to HIGH
    GPIO.output(pinTrigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    startTime = time.time()
    stopTime = time.time()

    # save start time
    while 0 == GPIO.input(pinEcho):
        startTime = time.time()

    # save time of arrival
    while 1 == GPIO.input(pinEcho):
        stopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = stopTime - startTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print ("Distance: %.1f cm" % distance)
    time.sleep(1)
    
    if distance<=90:
                print("Taking Picture")
                #with picamera.PiCamera() as camera:
                camera=picamera.PiCamera()
                camera.capture("image.jpg")
                #GPIO.cleanup() 
                print("Picture Taken")
                camera.close()
                time.sleep(20)
                storage.child("Images/test.jpg").put("image.jpg")
                print("Image sent to Firebase")
                time.sleep(15)
                retrieve()
                
                

    #if (distance<=90):
        #       print("Taking Picture")
        #      camera=picamera.PiCamera()
        #     camera.capture("/home/pi/Desktop/Images from PiCam/image.jpg")
        #    print("Picture Taken")
        #   flag=0

    

#GPIO.cleanup()
