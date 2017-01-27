import cv2, pickle, numpy as np, os
from fetures_by_profilling import feature_by_projection
from collections import defaultdict
from MooreNeibhourTracing import moore
from features_by_box_method import feture_by_box
from feature_extraction import LCS, zoning, characters


def classification_by_moore(img):
    features = pickle.load(open('H:\workspace\Projects\TextFromImage\moore-new-feature.np', 'rb'))
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    l, r = 60, 40
    dst = cv2.resize(img, (r, l))
    path = None
    for i in range(1, l - 1):
        for j in range(1, r - 1):
            if dst[i, j] == 0:
                path = moore([i, j], dst, dst[i, j])

        if path is not None:
            break
    ch = 0
    diff = LCS(path, features[0])
    for key in features.keys():
        cur = LCS(path, features[key])
        if cur > diff:
            diff = cur
            ch = key
    # print path
    return ch


def classification_by_zoning(img):
    features = pickle.load(open('H:\workspace\Projects\TextFromImage\zoning-feature.np', 'rb'))
    size = 4
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    flag = False
    l, r = 60, 40
    img = cv2.resize(img, (r, l))
    zone = zoning(img)
    chrs = [[0 for j in range(size)] for i in range(size)]

    diff = abs(zone - features[0])
    for key in features.keys():
        sz = abs(zone - features[key])
        for i in range(size):
            for j in range(size):
                if diff[i, j] > sz[i, j]:
                    diff[i, j] = sz[i, j]
                    chrs[i][j] = key

    chs = {}
    for i in range(size):
        for j in range(size):
            if not chs.has_key(chrs[i][j]):
                chs[chrs[i][j]] = 0
            chs[chrs[i][j]] += 1
    # print chs,
    chs = {chs[key]: key for key in chs.keys()}
    return chs[max(chs.keys())]


def check_box(a, b):
    size1 = 6
    size2 = 4
    cnt = 0
    for i in range(size1):
        for j in range(size2):
            if a[i, j] == b[i, j]:
                cnt += 1
    return cnt


def classification_by_box(img):
    features = pickle.load(open('H:\workspace\Projects\TextFromImage\moore-new-feature.np', 'rb'))
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    l, r = 60, 40
    img = cv2.resize(img, (r, l))
    actual = feture_by_box(img)
    diff = check_box(actual, features[0])
    ch = 0
    for key in features.keys():
        box = check_box(actual, features[key])
        cur = box
        if cur > diff:
            diff = cur
            ch = key
    print ch,


def compare_pixel(a, b):
    cnt1, cnt2 = 0, 0
    for i in range(60):
        for j in range(40):
            if a[i, j] == b[i, j]:
                cnt1 += 1
    return cnt1


def classification_by_pixel_matching(img):
    features = pickle.load(open('H:\workspace\Projects\TextFromImage\pixel-new-feature.np', 'rb'))
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    l, r = 60, 40
    img = cv2.resize(img, (r, l))
    diff = compare_pixel(img, features[0])
    # diff = diff[0]-diff[1]
    ch = 0
    for key in features.keys():
        match = compare_pixel(img, features[key])
        if match > diff:
            diff = match
            ch = key
    return ch


def check_projection(a, b):
    diff, ch = [], []
    for i in range(4):
        d, c = [], []
        for j in range(len(a[i])):
            d.append(abs(a[i][j] - b[i][j]))
            c.append(0)
        diff.append(d)
        ch.append(c)
    return diff, ch


def classification_by_projection(img):
    features = pickle.load(open('H:\workspace\Projects\TextFromImage\projection-new-feature.np', 'rb'))
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    l, r = 60, 40
    img = cv2.resize(img, (r, l))
    actual = feature_by_projection(img)
    diff, ch = check_projection(actual, features[0])
    for key in features.keys():
        for i in range(4):
            for j in range(len(actual[i])):
                smpl = abs(actual[i][j] - features[key][i][j])
                if smpl < diff[i][j]:
                    diff[i][j] = smpl
                    ch[i][j] = key

    ch_dict = defaultdict(int)
    for item in ch:
        for col in item:
            ch_dict[col] += 1
    ch_dict = {ch_dict[key]: key for key in ch_dict.keys()}
    return ch_dict[max(ch_dict.keys())]


if __name__ == "__main__":
    data = [-4496, -4535, 871, -4223]
    os.chdir('./character-database')

    for i in range(25, 66):
        ch = characters[i]
        print 'working on ', ch
        os.chdir('./' + str(i))
        k = 1
        for item in os.listdir(os.curdir):
            print 'item no.', k
            k += 1
            img = cv2.imread(item)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            p2 = classification_by_zoning(img)
            p3 = classification_by_pixel_matching(img)
            p4 = classification_by_projection(img)
            if p2 == ch:
                data[1] += 1
            else:
                data[1] -= 1

            if p3 == ch:
                data[2] += 1
            else:
                data[2] -= 1

            if p4 == ch:
                data[3] += 1
            else:
                data[3] -= 1

        os.chdir(os.pardir)
        print data
    print data
    file = open('re-enforcement.np', 'wb')
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
    file.close()
