#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# 0 laptop内置摄像头

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    print cap.get(3), cap.get(4)
    # 打印 宽度 高度 640 480
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()