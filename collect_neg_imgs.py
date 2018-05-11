# -*- coding: utf-8 -*-
# @Time    : 18-5-9 上午10:52
# @Author  : JeeShao
# @File    : collect_neg_imgs.py

import cv2
import numpy as np
import os

path = "./train_imgs/non-faces/"
i = 0
cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,1)
        # print frame.shape
        cv2.imshow("gray",frame)
        frame = cv2.resize(frame,(frame.shape[1]/4,frame.shape[0]/4),cv2.INTER_LINEAR) #高480x宽640 ==> 高120x宽160  shape=[高,宽]
        i+=1
        if i%5==0:
            cv2.imwrite(path+"%s.pgm"%(i/5),frame) #每5帧获取一张图片
            print i/5
        if cv2.waitKey(10) & 0xff == ord('q') or  i/5>500:
            break
        # this_dir = os.path.abspath(os.path.dirname(__file__))

cap.release()
cv2.destroyAllWindows()