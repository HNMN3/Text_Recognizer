__author__ = 'HNMN3'
import cv2,os
import copy
from collections import defaultdict
from sklearn.cluster import KMeans
import numpy as np
img = cv2.imread('4.jpg')

#1.threshing of imae
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg',gray)
l,r = gray.shape
ret,otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite('otsu-op.jpg',otsu)
dict = defaultdict(list)
labels = [[-1]*r]*l
cLable=1
for i in range(l):
    for j in range(r):
        list = []
        cl=gray[i,j]
        if i>0 and j>0 and gray[i-1][j-1] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i-1][j-1]))
        elif i>0 and gray[i-1][j] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i-1][j]))
        elif j>0 and gray[i][j-1]in range(cl-5,cl+6):
            list.append(copy.copy(labels[i][j-1]))
        elif i<l-1 and j>0 and gray[i+1][j-1] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i+1][j-1]))
        elif i<l-1 and j<r-1 and gray[i+1][j+1] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i+1][j+1]))
        elif i<l-1 and gray[i+1][j] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i+1][j]))
        elif j<r-1 and gray[i][j+1] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i][j+1]))
        elif i>0 and j<r-1 and gray[i-1][j+1] in range(cl-5,cl+6):
            list.append(copy.copy(labels[i-1][j+1]))
        flag=True

        if len(list)>0:
            lb = copy.copy(max(list))
        for item in list:
            if item>0 and item<=lb:
                lb=copy.copy(item)
                flag=False
        if flag:
            lb=copy.copy(cLable)
            cLable+=1
        labels[i][j]=copy.copy(lb)
        dict[copy.copy(lb)].append(copy.copy((i,j)))

ino=0
for item in dict.keys():
    white_image = np.zeros(img.shape)
    white_image[:,:] = 255
    if len(dict[item])<1000:
        continue
    for i,j in dict[item]:
        white_image[i,j]=0


    cv2.imwrite('image' + str(ino) + ".jpg",white_image)
    ino+=1




































'''lb=1
flag = [[True]*r]*l
max = l*r
done=0
dict = defaultdict(list)
i,j=0,0
while done<max:
    if i<l and j<r and flag[i][j]:
        done+=1
    else:
        i,j=0,0
        while i<l:
            while j<r:
                if flag[i][j]:
                    break
                j+=1
            if j<r:
                break
            i+=1
        continue
    dict[lb].append((i,j))
    cp=gray[i,j]
    flag[i][j]=False

    if i>0 and j>0 and gray[i-1,j-1]==cp:
        i-=1
        j-=1
    elif i>0 and gray[i-1,j]==cp:
        i-=1
    elif j>0 and gray[i,j-1]==cp:
        j-=1
    elif i<l-1 and j>0 and gray[i+1,j-1]==cp:
        i+=1
        j-=1
    elif i<l-1 and j<r-1 and gray[i+1,j+1]==cp:
        i,j=i+1,j+1
    elif i<l-1 and gray[i+1,j]==cp:
        i+=1
    elif j<r-1 and gray[i,j+1]==cp:
        j+=1
    elif i>0 and j<r-1 and gray[i-1,j+1]==cp:
        i-=1
        j+=1
    else:
        i,j=0,0
        while i<l:
            while j<r:
                if flag[i][j]:
                    break
                j+=1
            if j<r:
                break
            i+=1
        lb+=1

for flg in flag:
    for fg in flg:
        if fg:
            print('haha')
            break
for item in dict:
    white_image = np.zeros(img.shape)
    white_image[:,:] = 255
    for x,y in dict[item]:
        white_image[x,y] = 0
    cv2.imshow('image',white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''






'''for i in range(l):
    for j in range(r):
        label = [0]*4
        if j>0:
            label[0] = otsu[i,j-1]
        if i>0:
            label[1],label[2] = otsu[i-1,j-1],otsu[i-1,j]
        if j<r-1:
            label[3] = otsu[i-1,j+1]
        item=0
        while item < 4:
            if label[item]>0:
                otsu[i,j] = item
                break
            item+=1
        if item<4:
            otsu[i,j] = lb
            lb-=10
        print otsu[i,j],
    print

cv2.imwrite('temp.jpg',otsu)
'''












































































'''print(gray[300:320])
ret,bin_img = cv2.threshold(gray,zero,one,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
l,r = bin_img.shape
for i in range(l):
    k,j=0,0
    while j<r:
        if bin_img[i,j]==bin_img[i,k]:
            j+=1
            continue
        bin_img[i,k:j] = 0 if j-k>30 else bin_img[i,k:j]
        k=j
        j+=1



#2.finding controus
image,controus,heirarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#img = cv2.distanceTransform(bin_img,cv2.DIST_L1,3)
blank_img = np.zeros(img.shape[:2],np.uint8)
blank_img[:,:] = 255
i=0
for contour in controus:
    [x,y,w,h] = cv2.boundingRect(contour)

    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.drawContours(blank_img,controus,i,0,2)
    i+=1

cv2.imwrite("ot2.jpg",bin_img)
os.system("tesseract otsu.jpg otsu_data")

cv2.imshow('image',img)
#cv2.imshow("otsu",blank_img)
cv2.waitKey(0)'''