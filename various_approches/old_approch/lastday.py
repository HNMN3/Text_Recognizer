#Keep Coding And change the world and do not forget anything... Not Again..
import cv2
import numpy as np

def func(white,i,j,l,r):
    stck = {(i,j)}
    minx,miny,maxx,maxy = i,j,i,j
    pix=0
    que=[]
    cl = white[i,j]
    while len(stck)>0:
        i,j = stck.pop()
        if pix>50:
            white[i,j]=255
        else:
            que.append((i,j))
            pix+=1
        if i<minx:
            minx = i
        if i>maxx:
            maxx = i
        if j<miny:
            miny = j
        if j>maxy:
            maxy = j
        white[i,j]= -1
        if i>0 and j>0 and white[i-1][j-1] in {cl-1,cl,cl+1}:
            stck.add((i-1,j-1))
        if i>0 and white[i-1][j] in {cl-1,cl,cl+1}:
            stck.add((i-1,j))
        if j>0 and white[i][j-1] in {cl-1,cl,cl+1}:
            stck.add((i,j-1))
        if i<l-1 and j>0 and white[i+1][j-1] in {cl-1,cl,cl+1}:
            stck.add((i+1,j-1))
        if i<l-1 and j<r-1 and white[i+1][j+1] in {cl-1,cl,cl+1}:
            stck.add((i+1,j+1))
        if i<l-1 and white[i+1][j] in {cl-1,cl,cl+1}:
            stck.add((i+1,j))
        if j<r-1 and white[i][j+1] in {cl-1,cl,cl+1}:
            stck.add((i,j+1))
        if i>0 and j<r-1 and white[i-1][j+1] in {cl-1,cl,cl+1}:
            stck.add((i-1,j+1))

    if pix>50:
        for x,y in que:
            white[x,y]=255
    else:
        for x,y in que:
            white[x,y]=0
    return white
img = cv2.imread('1.jpg',0)
white = cv2.imread('4.jpg',0)
l,r = img.shape[:2]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(l):
    for j in range(r):
        if img[i,j]!=255:
            img = func(img,i,j,l,r)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()