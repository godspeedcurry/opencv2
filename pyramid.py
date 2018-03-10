#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np, sys
img = cv2.imread('test.png')

lower_reso = cv2.pyrUp(img)
cv2.imshow('image', lower_reso)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()