import cv2
import numpy as np
import pyzbar.pyzbar
import pyzbar.pyzbar as _pyzbar
import requests
import imutils

while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    decodedObjects = _pyzbar.decode(cap)
    for obj in decodedObjects:
        print("Data", obj.data)

    cv2.imshow("Baran", frame)
    key = cv2.waitKey(1)
    if key ==27:
        break

