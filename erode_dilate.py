#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('pf.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
# 腐蚀
dilation = cv2.dilate(img,kernel,iterations = 1)
# 膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 开运算 先腐蚀再膨胀

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 闭运算 先膨胀再腐蚀
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# 形态学梯度
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# 礼帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# 黑帽
cv2.imshow('image', blackhat)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()