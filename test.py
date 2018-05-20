# -*- coding: utf-8 -*-
# @Time    : 18-5-9 下午2:13
# @Author  : JeeShao
# @File    : test.py
import numpy
import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while True:

# img = cv2.imread('./train_imgs/orl_faces/s1/1.pgm')
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
    #-----------------------------------------
    # up half of the face is set to find eyes!
    #-----------------------------------------
        roi_gray = gray[y:y+h/2, x:x+w]
        roi_color = img[y:y+h/2, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    cv2.waitKey(10)
    print ("位置：",(x,y,w,h))
cv2.destroyAllWindows()