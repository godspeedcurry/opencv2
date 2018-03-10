#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100, (25, 2))
print trainData

responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red = trainData[responses.ravel()==0]

plt.scatter(red[:,0],red[:,1],80,'r','^')

blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

plt.show()