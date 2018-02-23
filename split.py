#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread('test.png')
b, g, r = cv2.split(img)
# 耗时的操作
img = cv2.merge(b, g, r)

b = img[:, :, 0]

# r通道设置为0
img[:, :, 2] = 0
