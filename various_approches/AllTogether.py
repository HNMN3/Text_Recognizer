# Keep Coding And change the world and do not forget anything... Not Again..
from DynamicThresh import D_ThreshBinary
from connectedComponents import connected_components
from BoundingRect import bounding_rect
import os, cv2, numpy as np, shutil


def func(filename='bjp.png'):
    dirname = filename[:filename.rindex('.')]

    # original image
    org = cv2.imread(filename)
    l, r = org.shape[:2]
    print(l, r)

    # Normalization
    m = 1000
    n = m * l / r
    l, r = n, m
    org = cv2.resize(org, (r, l))

    print(l, r)

    # for showing blocks
    blks = org.copy()

    # Reading image in grayscale/
    img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

    # changing directory
    if os.path.exists('./' + dirname):
        shutil.rmtree(dirname)

    while True:
        try:
            os.mkdir(dirname)
        except:
            continue
        break

    os.chdir(dirname)

    # saving images
    cv2.imwrite('original.jpg', org)
    cv2.imwrite('gray.jpg', img)
    # Thresholding
    img = D_ThreshBinary(img)
    # ret,img = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
    # saving binary image
    cv2.imwrite('binary.jpg', img)

    # initializing variables
    data_list = [[img[i, j] for j in range(r)] for i in range(l)]
    dd = 0
    s1, s2 = "", ""
    # splitting image and getting connected components
    for i in range(l):
        for j in range(r):
            if data_list[i][j] != 0:
                continue
            data_list, a, b, c, d = bounding_rect(data_list, i, j, l, r)

            # Removing unnecesary Blocks..
            if c - a > int(0.65 * l) or d - b > 900 or c - a < int(0.02 * l) or d - b < 70:
                continue

            if a > 1:
                a -= 1
            if b > 1:
                b -= 1
            if c < l - 1:
                c += 1

            if d < r - 1:
                d += 1
            dd += 1

            # creating rectangle
            cv2.rectangle(blks, (b, a), (d, c), (0, 0, 255), 2)

            # Saving image of block..
            cv2.imwrite('sample' + str(dd) + '.jpg', org[a:c, b:d])

            # Finding the connected components..
            smt = connected_components(cv2.imread('sample' + str(dd) + '.jpg'), 'sample' + str(dd))
            s1 += smt[0]
            s2 += smt[1]
            s1 += '\n'
            s2 += '\n'
            # os.chdir('..')

    file = open('output-by-sklearn.txt', 'w')
    file.write(s1)
    file.close()
    file = open('output-by-pix-matching.txt', 'w')
    file.write(s2)
    file.close()
    print
    dd
    cv2.imwrite('rectangle.jpg', blks)
    os.chdir(os.pardir)
    return blks


os.chdir('./temp')
for item in os.listdir(os.getcwd()):
    if item.endswith('jpg') or item.endswith('png'):
        print
        'working on', item
        func(item)
