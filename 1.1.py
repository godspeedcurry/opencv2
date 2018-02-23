#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ①图像处理技术： 图像压缩 增强和复原 匹配描述识别  3parts
# ②计算机视觉： 使机器“看”的科学 用摄像机和电脑代替人眼对目标进行识别
# 差别：①处理图像 ②模拟人的视觉
# Open Source Computer Vision Library
#
import numpy as np
import cv2

img = cv2.imread('test.png', 0)
img1 = cv2.imread('gray.png', cv2.IMREAD_COLOR)
# 读入彩色图像，ignore透明度
img2 = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
# 以灰度模式读入图像
img3 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
# read 包括图像的alpha通道
cv2.imwrite('gradescale.png', img2)
# 保存img2
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# add这句使得窗口大小可以调整
cv2.imshow('image', img1)
a = cv2.waitKey(0)
print a
# 键盘绑定函数，ms为单位，监测键盘输入，1s内有输入，返回该按键的ASCII值，无 return -1
# 0 无限期等待键盘输出
# function 检测某个按键是否被按下
cv2.destroyAllWindows()
