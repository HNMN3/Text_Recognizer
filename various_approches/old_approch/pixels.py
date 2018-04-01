#Keep Coding And change the world and do not forget anything... Not Again..
import cv2,os
import numpy as np
from collections import defaultdict
img = cv2.imread('1.jpg',0)
l,r = img.shape[:2]
dict = defaultdict(list)
for i in range(l):
    for j in range(r):
        color = img[i,j]
        for item in dict.keys():
            if abs(int(color-item))<150:
                color = item
                break
        dict[color].append((i,j))
kernel = np.ones((2,2),np.uint8)
i=0
for item in dict.keys():
    if len(dict[item])<500:
        continue
    white_image = np.zeros(img.shape)
    white_image[:,:] = 255
    for x,y in dict[item]:
        white_image[x,y] = 0
    cv2.dilate(white_image,kernel,iterations=1)

    cv2.imwrite('temp.jpg',white_image)
    os.system("tesseract temp.jpg data")
    fd = open("data.txt")
    fh = open("final" +str(i) + ".txt","w")
    data = fd.read()
    if len(data.strip())>0:
        fh.write(data)
        i+=1
    fh.close()
    cv2.imshow('image',white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



