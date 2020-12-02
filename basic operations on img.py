import numpy as np
import cv2

img= cv2.imread('messi5.jpg')

print(img.shape) #returns a tupple of rows columns and channels
print(img.size) #returns the total number of pixels accessed
print(img.dtype) #returns Image datatype 

b,g,r=cv2.split(img) #to split image into 3 channels
img=cv2.merge((b,g,r))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
