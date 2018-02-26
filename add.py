#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
# x = np.uint8([250])
# y = np.uint8([10])
# print cv2.add(x, y)
# # 250+10=260 最大255
# print x+y
# # 260%256=4

# mixed
# 加入了权重

img1 = cv2.imread('test.png')
img2 = cv2.imread('gradescale.png')

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()