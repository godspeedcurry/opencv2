#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
green=np.uint8([[[0,255,255]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green

