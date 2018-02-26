#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('test.png')

rows,cols = img.shape[:2]


M=cv2.getRotationMatrix2D((cols/2,rows/2),90,0.6)

dst = cv2.warpAffine(img,M,(2*cols,2*rows))

while 1:
    cv2.imshow('img',dst)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()