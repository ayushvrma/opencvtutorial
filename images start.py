import cv2
img=cv2.imread('lena.jpg')
cv2.imshow('result',img,)
k=cv2.waitKey(0) 

if k==27:
    cv2.destroyAllWindows()
if k==ord('s'):
    cv2.imwrite('lenacopy.png',img)
    cv2.destroyAllWindows()

