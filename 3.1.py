#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# name start point end point color(BGR) thickness
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 90, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
linetype = cv2.LINE_AA
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
