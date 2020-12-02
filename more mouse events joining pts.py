import numpy as np
import cv2

# events=[i for i in dir(cv2) if 'EVENT' in i]
# print (events)


# these parameters are same everywhere in mouse event
def click_event(event, x, y, flags, param):
    #joins points together
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))

        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0,255,255),1)
        cv2.imshow('image',img)


#img=np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena.jpg')
points=[]
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
