#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img1 = cv2.imread('test.png')
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
constant = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(232),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(233),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(234),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(235),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

# subplot是将多个图画到一个平面上的工具。
# 其中，m表示是图排成m行，n表示图排成n列，也就是整个figure中有n个图是排成一行的，一共m行，如果m=2就是表示2行图。

plt.show()
