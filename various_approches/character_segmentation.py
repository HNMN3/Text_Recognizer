# Keep Coding And change the world and do not forget anything... Not Again..
import os, cv2


def char_segment(img, dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)
    cv2.imwrite('original.jpg', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('otsu.jpg', dst)
    l, r = gray.shape[:2]
    k = 0
    seg = 1
    zr = [0] * l
    flag = True
    for j in range(r):
        i = 1
        cl = dst[0, j]
        while i < l and dst[i, j] == cl:
            i += 1

        if i == l and flag:
            segment = img[:, k:j]
            cv2.imwrite('segment' + str(seg) + '.jpg', segment)
            seg += 1
            k = j + 1
            flag = False
        if i != l:
            flag = True
