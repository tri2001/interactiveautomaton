# Interactive Automaton
# HACKTM project

import os
import io
import time
import cv2
import numpy
import readchar
from PIL import Image
import wiringpi

# Globals

CAPTURE_W = 640
CAPTURE_H = 480
CAPTURE_FPS = 1

# Init
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetmode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

# Methods

def show_main_menu():    
    option = -1
    while option < 0:
        
        os.system('clear')
        print("Autmatom v1\n")
        print("Options:\n")
        print("1: Start interacting")
        print("2: Test head move")
        print("\n0: Iesire")        
        try:
            option = int(input("\n\n--> "))
        except ValueError:
            option = -1
            
    return option

def interact():
    os.system('clear')
    print('Interacting started.... ')

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # start detecting faces
    camera = cv2.VideoCapture(0)

    while True:
        # get camera image
        ret, image = camera.read()
        
        # create grayscale image
        gs_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # all done! let's detect faces near the automaton!
        faces = face_cascade.detectMultiScale(gs_image, 1.1, 5);

        print("Detected faces : %d" %(len(faces)))

        # draw rectangles to highlight faces
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Frame", image)
        if(cv2.waitKey(1) == ord('q')) :
            break;

    camera.release()
    cv2.destroyAllWindows()

def test_move_head():    
    while True:
        for pulse in range(100,200,1):
            wiringpi.pwmWrite(18, pulse)
            time.sleep(0.01)
        for pulse in range(200,100,-1):
            wiringpi.pwmWrite(18, pulse)
            time.sleep(0.01)
    

# Go

option = -1

while option != 0:
    option = show_main_menu()

    if option == 0:
        exit()
    elif option == 1:
        interact()
    elif option == 2:
        test_move_head()

    option = -1
    
