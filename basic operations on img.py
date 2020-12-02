import numpy as np
import cv2

img= cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape) #returns a tupple of rows columns and channels
print(img.size) #returns the total number of pixels accessed
print(img.dtype) #returns Image datatype 

b,g,r=cv2.split(img) #to split image into 3 channels
img=cv2.merge((b,g,r))

ball=img[280:340,330:390] #top left and bottom right points to copy all the pixels of the ball
img[273:333,100:160]= ball  #co ordinates where to place the ball

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512)) 

dst= cv2.add(img,img2) #cant add 2 images of different sizes so make their sizes equal

#can use cv2.addWeighted()

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
