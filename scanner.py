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

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')       # coverts to barcode data to string

        # Creates box over the detected code
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1,1,2))
        cv.polylines(img, [points], True, (255,0,255), 5)   # polylines(filename, pts, IsClosed, Color, Thickness)
        
        # Puts text on top of the detected code
        points2 = barcode.rect
        cv.putText(img, myData, (points2[0], points2[1]), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        # prints the data of the code
        print(myData)

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
