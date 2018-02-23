#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.png', 0)
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.xticks([]), plt.yticks([])
# hide x,y坐标轴
plt.show()
# 彩色图像使用OpenCV 加载时是 BGR 模式。
# 但是 Matplotib 是 RGB 模式。所以彩色
# 图像如果已经被 OpenCV 读取，那它将不会
# 被 Matplotib 正确显示
# 比如你把默认参数改成cv2.IMREAD_COLOR
