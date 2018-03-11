#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image

area = 0
def ostu(img):
    global area
    image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转灰度
    blur = cv2.GaussianBlur(image,(5,5),0) # 阈值一定要设为 0 ！高斯模糊
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 二值化 0 = black ; 1 = white
    # cv2.imshow('image', th3)
    # a = cv2.waitKey(0)
    # print a
    height, width = th3.shape
    for i in range(height):
        for j in range(width):
            if th3[i, j] == 255:
                area += 1
    return area
