import numpy as np
import cv2
#img=cv2.imread('lena.jpg')

img=np.zeros([512,512,3],np.uint8) #to get a black image

img=cv2.line(img,(0,0),(255,300),(255,0,0),5) #color in bgr format

img=cv2.arrowedLine(img,(0,0),(100,200),(0,255,0),4)

#pt1 is top left, pt2 is bottom right
img=cv2.rectangle(img,(300,0),(244,100),(0,0,255),-1) #if u give thickness -1, it will fill the rect w the color

font=cv2.FONT_HERSHEY_COMPLEX_SMALL
img=cv2.putText(img,'oye oye',(10,500),font,4,(255,255,255),cv2.LINE_AA)
cv2.imshow('result',img)
cv2.waitKey(0)
