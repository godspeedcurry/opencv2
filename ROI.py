#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread('ball.png')

print img.shape
ball = img[190:250, 50:110]
img[70:130, 200:260]=ball
cv2.imshow('image', img)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()