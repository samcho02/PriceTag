import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode
from bs4 import BeautifulSoup as BS
import requests
import lxml

## video capture 
capture = cv.VideoCapture(0, cv.CAP_DSHOW)
# sets up the video window
capture.set(3, 640)    
capture.set(4, 480)    # height
myData = []
my = ''
url = "https://www.upcitemdb.com/upc/"
doc = None

## Scans barcode & stores the barcode to myData
def scan_barcode():
    while capture.isOpened():
        success, img = capture.read()

        for barcode in decode(img):
            while len(myData) == 0:
                myData.append(barcode.data.decode('utf-8'))      # coverts to barcode data to string

                if len(myData) == 1:
                    my = str(myData[0])
                    print(my)
                    url = "https://www.upcitemdb.com/upc/" + my
                    result = requests.get(url)
                    doc = BS(result.text, "lxml")

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


scan_barcode()

data = []
dict = {"Store": [], "Product": [], "Price": []}

## Web scrapes the product
def store_product_price(doc):
    table = doc.find("table", attrs={'class': 'list' ,'style':'width:100%;'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    
    # finds the colum td
    for row in rows:
        colums = row.findAll('td')
        colums = [ele.text.strip() for ele in colums]
        data.append([ele for ele in colums if ele])
        
    # Adds Store, Product, Price data to dictionary
    for list in data:

        dict["Store"].append(list[0])
        dict["Product"].append(list[1])
        dict["Price"].append(list[2])
        
    print(dict)

## Calls
store_product_price(doc)