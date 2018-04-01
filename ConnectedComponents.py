# Keep Coding And change the world and do not forget anything... Not Again..
import os, cv2

bsh = []
image_real = None
lines = {}
lino = 0


def separates(white, i, j, l, r):
    global bsh, lino
    a, b, c, d = i, j, i, j
    stck = {(i, j)}
    frq = 0
    cl = white[i][j]
    pix = 0
    # flood fill on 8-side
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

    # mainting line number
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

    a = max(1, a - 1)
    b = max(1, b - 1)
    c = min(c + 1, l - 1)
    d = min(d + 1, r - 1)

    bsh.append((b, yno, image_real[a:c, b:d]))
    return white


def connected_components(img):
    global bsh, image_real, lines, lino
    bsh = []
    lines = {}
    lino = 0

    # convert image into binary
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    black_pixels = (dst == 0).sum()
    white_pixels = (dst == 255).sum()
    if black_pixels > white_pixels:
        ret, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

    # find all charactrs
    l, r = dst.shape[:2]
    data_list = map(list, dst)
    image_real = dst.copy()
    for i in range(l):
        for j in range(r):
            if data_list[i][j] != 0:
                continue
            data_list = separates(data_list, i, j, l, r)
    return bsh


def traverse_dir(directory):
    os.chdir(directory)
    for item in os.listdir('.'):
        print('Working on {}'.format(item))
        # smpldir = item[:item.rindex('.')]
        # os.mkdir(smpldir)
        img = cv2.imread(item)
        cv2.imwrite('original.jpg', img)
        x, y, cvt_img = connected_components(img)[0]
        cv2.imwrite('converted.jpg', cvt_img)
    os.chdir('..')


if __name__ == "__main__":
    traverse_dir('temp')
