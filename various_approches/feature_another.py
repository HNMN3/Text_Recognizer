import cv2, pickle
from MooreNeibhourTracing import moore

if __name__ == "__main__":
    data = pickle.load(open('features-another.np', "rb"))
    for key in data.keys():
        data[key] = data[key][:20]

    print data

    flag = 1

    while flag:
        path = raw_input('Enter path\n')
        dst = cv2.imread(path, 0)
        if dst is None:
            continue
        l, r = dst.shape[:2]
        flag = False
        for i in range(l):
            for j in range(r):
                if dst[i, j] == 0:
                    tpath = moore([i, j], dst, dst[i, j])

                    flag = True
                    break
            if flag:
                break

        if len(tpath) < 20:
            path = raw_input('enter another path')
        else:
            ch = raw_input('Enter character\n')
            data[ch] = tpath
            flag = int(raw_input('Another image?(1/0)'))

    file = open('features-another.np', 'wb')
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
    file.close()
