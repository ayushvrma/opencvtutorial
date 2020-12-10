""" 
a process to proccess images to different sizes 

2types of pyramids: gaussian and laplasian
"""


import cv2
import numpy as np
img = cv2.imread("lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer) #to reduce the resolution of the image
    gaussian_pyramid_list.append(layer)
    #cv2.imshow(str(i), layer)

""" a laplasian pyramid is formed by the difference btwn that level in gaussian pyramid and expanded
version of its upper level in gaussian pyramid

its used for edge detection by blending images"""

layer = gaussian_pyramid_list[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
