#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127, 255, 0)
image,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
area = cv2.contourArea(cnt)

M = cv2.moments(cnt)
# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
# print M
# print cx
# print cy
# print cnt
cv2.imshow('image', approx)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()