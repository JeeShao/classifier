#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 21:10
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : demo.py
# -*- coding: utf-8 -*-
# @Time    : 18-5-9 下午2:13
# @Author  : JeeShao
# @File    : test.py
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('./classifier/cascade.xml')
# eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
# cap = cv2.VideoCapture(0)
# while True:

img = cv2.imread('./train_imgs/45.png',0)
    # ret,img = cap.read()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img, 1.2, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)
