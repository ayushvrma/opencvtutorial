""" canny edge detector is an edge detection operator that uses a multi-stage algo to detect wide range of edges in images.

5 steps:
1: noise reduction
2: gradient calculation
3: non-maximum supression
4. double threshold
5. edge tracking by hystheris """

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img, 100, 200) #threshold values for hystheris procedurem usually use a trackbar

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
