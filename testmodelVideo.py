import cv2
import numpy as np

waterloo_card_cascade = cv2.CascadeClassifier('models/TrainModel7/cascade.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # image, reject levels level weights.
    watches = waterloo_card_cascade.detectMultiScale(gray, 5,5)
    # add this
    for (x,y,w,h) in watches:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()