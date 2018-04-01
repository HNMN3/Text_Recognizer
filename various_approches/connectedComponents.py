# Keep Coding And change the world and do not forget anything... Not Again..
import os, cv2, copy, cv
from classification import classification_by_pixel_matching
from classification_sklearn import classify
import numpy as np

bsh = []
image_real = None
lines = {}
lino = 0


def seprates(white, i, j, l, r):
    global bsh, lino
    a, b, c, d = i, j, i, j
    stck = {(i, j)}
    frq = 0
    cl = white[i][j]
    pix = 0
    while len(stck) > 0:
        frq += 1
        i, j = stck.pop()
        a, b, c, d = min(i, a), min(j, b), max(i, c), max(j, d)
        white[i][j] = -1
        pix += 1
        if i > 0 and j > 0 and white[i - 1][j - 1] == cl:
            stck.add((i - 1, j - 1))
        if i > 0 and white[i - 1][j] == cl:
            stck.add((i - 1, j))
        if j > 0 and white[i][j - 1] == cl:
            stck.add((i, j - 1))
        if i < l - 1 and j > 0 and white[i + 1][j - 1] == cl:
            stck.add((i + 1, j - 1))
        if i < l - 1 and j < r - 1 and white[i + 1][j + 1] == cl:
            stck.add((i + 1, j + 1))
        if i < l - 1 and white[i + 1][j] == cl:
            stck.add((i + 1, j))
        if j < r - 1 and white[i][j + 1] == cl:
            stck.add((i, j + 1))
        if i > 0 and j < r - 1 and white[i - 1][j + 1] == cl:
            stck.add((i - 1, j + 1))
    yno = -1
    for ln in range(1, lino + 1):
        if c < lines[ln][0] or a > lines[ln][1]:
            continue
        else:
            yno = ln
            break
    if a == 0 and b == 0 and c == l - 1 and d == r - 1:
        yno = 0
    elif yno == -1:
        lino += 1
        yno = lino
        lines[yno] = [a, c]
    else:
        lines[yno][0] = min(a, lines[yno][0])
        lines[yno][1] = max(c, lines[yno][1])

    if a > 1:
        a -= 1

    if b > 1:
        b -= 1

    if c < l - 1:
        c += 1

    if d < r - 1:
        d += 1

    bsh.append((b, yno, image_real[a:c, b:d]))
    return white


def connected_components(img, dirname):
    global bsh, image_real, lines, lino
    bsh = []
    lines = {}
    lino = 0
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    os.chdir(dirname)
    # cv2.imwrite('original.jpg',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    hist = cv.calcHist([dst], [0], None, [256], [0, 256])
    if hist[0] > hist[255]:
        ret, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
    # cv2.imwrite('otsu.jpg',dst)
    l, r = dst.shape[:2]
    fno = 1
    datas = [[dst[i, j] for j in range(r)] for i in range(l)]
    image_real = copy.copy(dst)
    for i in range(l):
        for j in range(r):
            if datas[i][j] != 0:
                continue
            datas = seprates(datas, i, j, l, r)

    bsh = sorted(bsh, key=lambda x: x[0])
    bsh = sorted(bsh, key=lambda x: x[1])
    y = 0
    s1 = ""
    s2 = ""
    cw = 0
    jth = 0
    for item in bsh:
        if item[1] != y:
            cw = 0
            fno = 1
            y = item[1]
            s1 += '\n'
            s2 += '\n'
        if cw == 0:
            cw = item[2].shape[1]
            # print cw
        elif bsh[jth][0] - bsh[jth - 1][0] - bsh[jth - 1][2].shape[1] > 0.4 * cw:
            s1 += " "
            s2 += " "
            fno += 1
        cv2.imwrite(str(item[1]) + '-' + str(fno).rjust(4, '0') + '.jpg', item[2])
        s1 += str(classify(item[2]))
        s2 += str(classification_by_pixel_matching(item[2]))
        fno += 1
        jth += 1
    os.chdir('..')
    return s1, s2


def traverseDir(dir):
    os.chdir(dir)
    for item in os.listdir('.'):
        smpldir = item[:item.rindex('.')]
        os.mkdir(smpldir)
        print connected_components(cv2.imread(item), smpldir)
    os.chdir('..')


if __name__ == "__main__":
    traverseDir('./just')
