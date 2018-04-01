import numpy as np, cv, cv2,math


def feture_by_box(img):
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    size1 = 6
    size2 = 4
    data = np.zeros((size1, size2))
    l, r = img.shape[:2]
    stepp, stepq = int(0.5 + l / size1), int(0.5 + r / size2)
    p = stepp
    pp, i = 0, 0
    while i < size1:
        q, qq, j = stepq, 0, 0
        while j < size2:
            sum=0
            for x in range(pp,p):
                for y in range(qq,q):
                    if img[x,y]==0:
                        sum += math.sqrt(x*x + y*y)

            sum = sum / ((q-qq)*(p-pp))
            '''hist = cv.calcHist([img[pp:p, qq:q]], [0], None, [256], [0, 256])
            if hist[0] > hist[255]:
                data[i, j] = 1
            else:
                data[i, j] = 0'''
            data[i,j] = sum
            j += 1
            qq = q
            q += stepq
            if q > r:
                q = r
        pp = p
        i += 1
        p += stepp
        if p > l:
            p = l

    return data
