import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

## video capture 
capture = cv.VideoCapture(0, cv.CAP_DSHOW)
# sets up the video window
capture.set(3, 640)    
capture.set(4, 480)    # height
myData = []
my = ''

## Scans barcode & stores the barcode to myData
def scan_barcode():
    while capture.isOpened():
        success, img = capture.read()

        for barcode in decode(img):
            while len(myData) == 0:
                myData.append(barcode.data.decode('utf-8'))      # coverts to barcode data to string

                if len(myData) == 1:
                    my = str(myData[0])
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

# ## Call
# scan_barcode()