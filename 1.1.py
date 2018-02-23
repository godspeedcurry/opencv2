#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('test.png', 0)
img = cv2.imread('test.png', 'COLOR')
img1 = cv2.imread_GRAYSCALE('test.png', 0)
img2 = cv2.imread_UNCHANGED('test.png', 0)

print img, img1, img2