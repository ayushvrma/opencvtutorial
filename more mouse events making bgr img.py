import numpy as np
import cv2

# events=[i for i in dir(cv2) if 'EVENT' in i]
# print (events)


# these parameters are same everywhere in mouse event
def click_event(event, x, y, flags, param):
    #joins points together

    if event == cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        mycolorimg= np.zeros((512,512,3),np.uint8)

        #[:] fills the whole image from start to end
        mycolorimg[:]= [blue,green,red]
        cv2.imshow('image', mycolorimg)


#img=np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
