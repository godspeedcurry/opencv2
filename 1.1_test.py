#! /usr/bin/env python
# -*- coding: utf-8 -*-
# todo 加载一个灰度图，显示图片，按下s保存后退出，按esc退出不保存

import cv2
img = cv2.imread('test.png', 0)
# or img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
a = cv2.waitKey(0)
# ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符他的输入时数字
if a == ord('s'):
    cv2.imwrite('gray.png', img)
    cv2.destroyAllWindows()
elif a == 27:
    cv2.destroyAllWindows()