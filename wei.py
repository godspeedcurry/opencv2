#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread('test.png')
img2 = cv2.imread('biao.png')
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# 在img1中标定要添加img2的位置

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# convert into gray img
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
# cv2.imshow('image', img2_fg)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1_bg)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()