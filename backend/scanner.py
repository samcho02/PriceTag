## Testing Ground
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

myData = []


def scanner():
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    cap.set(3,640)
    cap.set(4,480)

    while True:
        ret, img = cap.read()

        if len(decode(img)) != 0:
            for barcode in decode(img):
                myData.append(barcode.data.decode('utf-8'))

            global my
            my = myData[0]
            
            print(myData)
            print(my)
            return False
        
        else:
            cv.imshow('test',img)

        # can always break out by pressing 'esc' key
        c = cv.waitKey(1)
        if c == 27:
            break
        
    cap.release()
    cv.destroyAllWindows()
    
scanner()
