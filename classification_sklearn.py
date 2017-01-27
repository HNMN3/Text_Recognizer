# Keep coding and change the world..And do not forget anything..Not Again..
import os
import cv2
import numpy as np
from skimage.feature import hog
from sklearn.externals import joblib


def classify(img, clf=joblib.load("characters_nn_extended100.pkl")):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    img = cv2.resize(img, (28, 28))
    img = cv2.dilate(img, (3, 3))
    hog_fd = hog(img, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1),
                 visualise=False)
    ch = clf.predict(np.array([hog_fd], 'float64'))
    return ch[0][0]


if __name__ == '__main__':
    b = "1"
    s = ""
    os.chdir('./testing/skit/sample4/')
    prev = None
    for item in os.listdir(os.curdir):
        if prev is None:
            prev = int(item[item.rindex('-') + 1:item.rindex('.')])
        else:
            cur = int(item[item.rindex('-') + 1:item.rindex('.')])
            if cur - prev > 1:
                s += " "
            prev = cur
        if not item.startswith(b):
            s += '\n'
            b = item[0]
        s += str(classify(cv2.imread(item, 0)))
    print s
