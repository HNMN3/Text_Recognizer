# Keep Coding And change the world and do not forget anything... Not Again..
import cv2
import numpy as np


def run_length(gray, l, r):
    white = np.zeros(gray.shape)
    white[:, :] = 255
    for i in range(l):
        k, j = 0, 0
        while j < r:
            if gray[i, j] == gray[i, k]:
                j += 1
                continue
            white[i, k:j] = (0 if j - k > 20 else gray[i, k:j])
            k = j
            j += 1
    for j in range(r):
        k, i = 0, 1
        while i < l:
            if gray[i, j] == gray[k, j]:
                i += 1
                continue
            white[k:i, j] = (0 if i - k > 40 else gray[k:i, j])
            k = i
            i += 1
    cv2.imshow('window', white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('1.jpg', 0)
run_length(img, *img.shape[:2])
