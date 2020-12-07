import numpy as np
import cv2 as cv


def nothing(x):
    print(x)


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image') #creates a named window, with different names

cv.createTrackbar('B', 'image', 0, 255, nothing) #name unique to trackbar
cv.createTrackbar('G', 'image', 0, 255, nothing)# nothing is a callback function, jisko bulayega after creating a trackbar
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('B', 'image') #to see the results of the trackbar
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
       img[:] = 0
    else:
       img[:] = [b, g, r] #set the bgr values according to trackbar


cv.destroyAllWindows()
