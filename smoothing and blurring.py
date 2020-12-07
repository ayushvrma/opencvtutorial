#smoothing is done to remove noise in images


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel) #homogenous is the most basic one, avg of pixels in kernal neighbours, 
#filter2d is used for homogeous filter

blur = cv2.blur(img, (5, 5))

gblur = cv2.GaussianBlur(img, (5, 5), 0) #gaussian blur uses different weighted kernels in both x and y direction

median = cv2.medianBlur(img, 5) #replaces every pixel value with median of its neighbouring pixels, 
#GREAT WHEN USING SALT AND PEPPER NOISE

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()