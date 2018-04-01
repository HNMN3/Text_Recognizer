import cv2, numpy as np, os, pickle, cv
from MooreNeibhourTracing import moore
from fetures_by_profilling import feature_by_projection

characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '-', '&', '@']
data = {}


def zoning(img):
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    size = 4
    data = np.zeros((size, size))
    l, r = img.shape[:2]
    step_p, step_q = int(0.5 + l / 6), int(0.5 + r / 6)
    p = step_p
    pp, i = 0, 0
    while i < size:
        q, qq, j = step_q, 0, 0
        while j < size:
            hist = cv.calcHist([img[pp:p, qq:q]], [0], None, [256], [0, 256])
            data[i, j] = hist[0] / ((p - pp) * (q - qq))
            j += 1
            qq = q
            q += step_q
            if q > r:
                q = r
        pp = p
        i += 1
        p += step_p
        if p > l:
            p = l

    return data


def LCS(str1, str2):
    if str2 is None or str1 is None:
        return "", 0

    m, n = len(str1), len(str2)
    arr = np.zeros((m + 1, n + 1))
    brr = np.zeros((m + 1, n + 1))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                arr[i, j] = arr[i - 1, j - 1] + 1
                brr[i, j] = 1
            elif arr[i - 1, j] > arr[i, j - 1]:
                arr[i, j] = arr[i - 1, j]
                brr[i, j] = 0
            else:
                arr[i, j] = arr[i, j - 1]
                brr[i, j] = 2

    fstr = ""
    i, j = m, n
    while i > 0 and j > 0:
        if brr[i, j] == 1:
            fstr += str(str1[i - 1])
            i, j = i - 1, j - 1
        elif brr[i, j] == 0:
            i -= 1
        else:
            j -= 1

    return fstr[::-1], arr[m, n]


if __name__ == '__main__':
    pass
