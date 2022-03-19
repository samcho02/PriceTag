import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

## video capture 
capture = cv.VideoCapture(0)
# sets up the video window
capture.set(3, 640)    
capture.set(4, 480)    # height
myData = []

## Scans barcode & stores the barcode to myData
def scan_barcode():
    while capture.isOpened():
        success, img = capture.read()

        for barcode in decode(img):
            if len(myData) == 0:
                myData.append(barcode.data.decode('utf-8'))      # coverts to barcode data to string
            # prints the data of the code
                print(myData)

            else:
                break
        

        # displays img in the Scanner window
        cv.imshow('Scanner', img)

        # waits for key to pressed for 1 ms
        c = cv.waitKey(1)       

        # if the key pressed is esc, break loop
        if c == 27:              
            break


## closes the vid cam
    capture.release()
    cv.destroyAllWindows()

## Call
scan_barcode()