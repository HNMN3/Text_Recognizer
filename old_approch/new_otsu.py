#Keep Coding And change the world and do not forget anything... Not Again..
import cv2
import numpy as np
import os

image = cv2.imread("/Workspace/Projects/TextFromImage/cutted.jpg",0)
retval,image = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)
image  =cv2.dilate(image,kernel,iterations=1)
cv2.imwrite('cutted-black.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('imp2.jpg',image)