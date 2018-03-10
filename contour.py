#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
im = cv2.imread('wlj.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
img = cv2.drawContours(image, contours, 3, (0,255,0), 3)
cv2.imshow('image', img)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()