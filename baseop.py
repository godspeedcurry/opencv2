#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread('test.png')
px = img[10, 100]
print px
# [ 89  87 196]
blue = img[10, 100, 0]
# bgr   返回第一个值
print blue
# change color
# img[100, 100] = [255, 255, 255]
# print img[100,100]

print img.item(10, 100, 0)
print img.item(10, 100, 1)
print img.item(10, 100, 2)

img.itemset((10, 100, 2), 100)
print img.item(10, 100, 2)

# obtain the attribute of an image
# rows /columns/ alpha /data type /number of px
print img.shape
# 行数 列数 通道数
# 灰度图只有行+列
# judge 彩色图还是灰色图
print img.size
# 像素数目
print img.dtype
# 数据类型 uint8

