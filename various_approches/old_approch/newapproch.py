#Keep Coding And change the world and do not forget anything... Not Again..
__author__ = 'HNMN3'
import copy as cp
import cv2,os
import copy
from collections import defaultdict
from sklearn.cluster import KMeans
import numpy as np
img = cv2.imread('1.jpg')

#1.threshing of imae
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
l,r = gray.shape


'''white = np.zeros(gray.shape)
white[:,:] = 255
for i in range(l):
    for j in range(r):
        list = []
        if i>0 and j>0:
            list.append(gray[i-1][j-1])
        elif i>0:
            list.append(gray[i-1][j])
        elif j>0:
            list.append(gray[i][j-1])
        elif i<l-1 and j>0:
            list.append(gray[i+1][j-1])
        elif i<l-1 and j<r-1:
            list.append(gray[i+1][j+1])
        elif i<l-1:
            list.append(gray[i+1][j])
        elif j<r-1:
            list.append(gray[i][j+1])
        elif i>0 and j<r-1:
            list.append(gray[i-1][j+1])
        t=0
        while t<len(list):
            if list[t] != gray[i,j]:
                break
            t+=1
        white[i,j] = (255 if t==len(list) else 0)
kernel = np.ones((5,5),np.uint8)
cv2.dilate(white,kernel,iterations=5)

'''











#run length top-bottom and left-right side in gray image
white = np.zeros(gray.shape)
white[:,:] = 255
for i in range(l):
    k,j=0,0
    while j<r:
        if gray[i,j]==gray[i,k]:
            j+=1
            continue
        white[i,k:j] = (0 if j-k>40 else 255)
        k=j
        j+=1
for j in range(r):
    k,i=0,1
    while i<l:
        if gray[i,j]==gray[k,j]:
            i+=1
            continue
        white[k:i,j] = (0 if i-k>40 else gray[k:i,j])
        k=i
        i+=1





kernel = np.ones((3,3),np.uint8)
white = cv2.erode(white,kernel,iterations=2)
white = cv2.dilate(white,kernel,iterations=2)
cv2.imwrite('ibinary.jpg',white)



def func(white,i,j):
    stck = {(i,j)}
    minx,miny,maxx,maxy = i,j,i,j
    while len(stck)>0:
        i,j = stck.pop()
        if white[i,j]==0:
            continue
        if i<minx:
            minx = i
        if i>maxx:
            maxx = i
        if j<miny:
            miny = j
        if j>maxy:
            maxy = j
        white[i,j]=0
        if i>0 and j>0 and white[i-1][j-1]==255:
            stck.add((i-1,j-1))
        if i>0 and white[i-1][j]==255:
            stck.add((i-1,j))
        if j>0 and white[i][j-1]==255:
            stck.add((i,j-1))
        if i<l-1 and j>0 and white[i+1][j-1]==255:
            stck.add((i+1,j-1))
        if i<l-1 and j<r-1 and white[i+1][j+1]==255:
            stck.add((i+1,j+1))
        if i<l-1 and white[i+1][j]==255:
            stck.add((i+1,j))
        if j<r-1 and white[i][j+1]==255:
            stck.add((i,j+1))
        if i>0 and j<r-1 and white[i-1][j+1]==255:
            stck.add((i-1,j+1))
    return white,minx,miny,maxx,maxy
fno =0
ffinal = open('final.txt','w')
for i in range(l):
    for j in range(r):
        if white[i,j]==0:
            continue
        white,y1,x1,y2,x2 = func(white,i,j)
        w = x2-x1
        h = y2-y1
        if w<30 or h<20:
            continue
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),2)

ffinal.close()
'''l,r = hsv.shape[:2]
cl=1
rng = set()
[rng.add(x) for x in hsv[0]]
[rng.add(x) for x in hsv[l-1]]
[(rng.add(hsv[i][0]),rng.add(hsv[i][r-1])) for i in range(l)]
kernel = np.ones((2,2),np.uint8)
white_image = np.zeros(img.shape)
white_image[:,:] = 255
lst = range(r)
print(len(rng))
for i in range(1,l):
    j,l1 = 0,len(lst)
    while j<l1:
        if hsv[i,j] in rng:
            lst.pop(j)
            l1-=1
            white_image[i,j]=0
        else:
            j+=1
#white_image = cv2.erode(white_image,kernel,iterations=1)
#white_image = cv2.dilate(white_image,kernel,iterations=1)



cv2.imshow('image',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

i=0
ffinal = open("final.txt","w")
for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),255,2)
    sample = gray[y:y+h,x:x+w]
    sample = cv2.resize(sample,(0,0),fx=5.0,fy=5.0)
    cv2.imwrite("sample.jpg",sample)
    #os.system("tesseract sample.jpg data")
    with open("data.txt") as fh:
        data = fh.read()
        ffinal.write(data)
    fh.close()
    i+=1'''
cv2.imwrite('temp.jpg',img)
#image = cv2.imread('temp.jpg',0)
#os.system("tesseract temp.jpg data")
'''cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

_,controus,_ = cv2.findContours(image,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
#print controus
for contour in controus:
    [x,y,w,h] = cv2.boundingRect(contour)
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
'''