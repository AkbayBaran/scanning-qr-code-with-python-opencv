# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import pyzbar.pyzbar
import pyzbar.pyzbar as _pyzbar

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.43.1:8080/shot.jpg"

# While loop to continuously fetching data from the Url
while True:

    img_resp = requests.get(url)
    cap =
    ret, frame = img_resp.read()
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=600, height=800)
    decodedObjects = _pyzbar.decode(img_resp)
    for obj in decodedObjects:
        print("Data", obj.data)
    cv2.imshow("Android_cam", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
