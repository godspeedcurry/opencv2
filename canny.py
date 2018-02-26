#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('wlj.png',0)
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
edges = cv2.Canny(closing,100,200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('edge'), plt.xticks([]), plt.yticks([])

plt.show()