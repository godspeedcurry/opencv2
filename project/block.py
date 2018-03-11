#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 判断木块颜色
import cv2
import numpy as np
import ostu
path = './block/red.png'
img = cv2.imread(path)
color = [100,130,50,100,20,45,0,10]
str_color = ['blue', 'green', 'yellow', 'red']
max_area = 1000
final = ''


def block(image):
    hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    global max_area
    global final
    for i in range(4):
        lower_color = np.array([color[2*i], 50, 50])
        upper_color = np.array([color[2*i+1], 255, 255])
        mask = cv2.inRange(hsv, lower_color, upper_color)
        res = cv2.bitwise_and(img, img, mask=mask)
        a = ostu.ostu(res)
        if max_area < a:
            max_area = a
            final = str_color[i]

block(img)
print final
print max_area
# #设定蓝色的阈值
# lower_blue=np.array([100,50,50])
# upper_blue=np.array([130,255,255])
#
# #设定绿色的阈值
# lower_green=np.array([50,50,50])
# upper_green=np.array([100,255,255])
#
# #设定黄色的阈值
# lower_yellow=np.array([20,50,50])
# upper_yellow=np.array([45,255,255])
#
# #设定红色的阈值
# lower_red=np.array([0,50,50])
# upper_red=np.array([10,255,255])
#根据阈值构建掩模
# mask=cv2.inRange(hsv,lower_blue,upper_blue)
# mask=cv2.inRange(hsv,lower_green,upper_green)
# mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
# mask=cv2.inRange(hsv,lower_red,upper_red)
# #对原图像和掩模进行位运算
# res=cv2.bitwise_and(img,img,mask=mask)
#
# cv2.imshow('image', res)
# a = cv2.waitKey(0)
# print a