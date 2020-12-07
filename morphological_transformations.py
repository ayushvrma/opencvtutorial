#morphological transformations are basic operations on images based on shapes
#normally performed on a binary image
#2 things req- original image and kernal to know what operation have to be done

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2) #to fill the pixels selected by kernals

erosion = cv2.erode(mask, kernal, iterations=1) #outer surface/boundary erode krdeta

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) #opening is just another name for erosion followed by dilation

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) #closing is just dilation then erosion

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal) #difference between dilation and erosion, gradient technique

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal) #top-hat technique

titles = ['image', 'mask', 'dilation',
          'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
