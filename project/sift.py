#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import datetime
starttime = datetime.datetime.now()

MIN_MATCH_COUNT = 10
name = 'apple0.png'
img1 = cv2.imread('./img/'+name, 0)  # targetImage
# cv2.imshow('image', img1)
# a = cv2.waitKey(0)
# print a
result = ''
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
#  定义比较函数，与所有图像比较
def compare(filename):
    global MIN_MATCH_COUNT
    global result
    global kp1, des1
    if filename != name:
        img2 = cv2.imread('./img/'+filename, 0)  # trainImage
        # find the keypoints and descriptors with SIFT
        kp2, des2 = sift.detectAndCompute(img2, None)
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)
        # store all the good matches as per Lowe's ratio test.
        good = []
        for m, n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
        if len(good) > MIN_MATCH_COUNT:  # 获取关键点的坐标
            MIN_MATCH_COUNT=len(good)
            result=filename
    return 0
for filename in os.listdir(r'./img'):
    compare(filename)
print filter(lambda x: x not in '0123456789', result[:-4])
print 'count='+str(MIN_MATCH_COUNT)
endtime = datetime.datetime.now()
print 'time='+str((endtime - starttime).seconds)+'s'