import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

## video capture 
capture = cv.VideoCapture(0)

# sets up the video window
capture.set(3, 640)
capture.set(4, 480)

while True:
    success, img = capture.read()
    cv.imshow('Result', img)

    for barcode in decode(img):
            myData = barcode.data.decode('utf-8')       # coverts to barcode data to string
            print(myData)

            points = np.array([barcode.polygon], np.int32)
            points = points.reshape[-1,1,2]
            
            cv.polylines(img, [points], True, (255,0,255), 5)   # polylines(filename, pts, IsClosed, Color, Thickness)
    
    
    c = cv.waitKey(1)           
    if c == 27:               # if the key pressed is esc, break loop
        break


## closes the vid cam
capture.release()
cv.destroyAllWindows()
