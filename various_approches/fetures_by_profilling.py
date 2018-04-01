import cv, cv2, numpy as np


def vertical(img):
    l, r = img.shape[:2]
    data = []
    for j in range(r):
        hist = cv.calcHist([img[:, j]], [0], None, [256], [0, 256])
        data.append(int(hist[0][0]))
    return data


def horizontal(img):
    l, r = img.shape[:2]
    data = []
    for i in range(l):
        hist = cv.calcHist([img[i, :]], [0], None, [256], [0, 256])
        data.append(int(hist[0][0]))
    return data


def diagonal1(img):
    l, r = img.shape[:2]
    data = []
    k = 0
    for i in range(l - 1, 0, -1):
        data.append(0)
        a, b = i, 0
        while a < l and b < r:
            if img[a, b] == 0:
                data[k] += 1
            a += 1
            b += 1
        k += 1
    for j in range(r):
        a, b = 0, j
        data.append(0)
        while a < l and b < r:
            if img[a, b] == 0:
                data[k] += 1
            a += 1
            b += 1
        k += 1
    return data


def diagonal2(img):
    l, r = img.shape[:2]
    data = []
    k = 0
    for j in range(r):
        a, b = 0, j
        data.append(0)
        while a < l and b >= 0:
            if img[a, b] == 0:
                data[k] += 1
            a += 1
            b -= 1
        k += 1
    for i in range(l):
        data.append(0)
        a, b = i, r-1
        while a < l and b >= 0:
            if img[a, b] == 0:
                data[k] += 1
            a += 1
            b -= 1
        k += 1

    return data


def feature_by_projection(img):
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    return [vertical(img),horizontal(img),diagonal1(img),diagonal2(img)]

if __name__=="__main__":
    img = cv2.imread(r"H:\workspace\Projects\TextFromImage\testing\aksh\sample7\1-0002.jpg",0)
    img = cv2.resize(img,(40,60))
    print feature_by_projection(img)