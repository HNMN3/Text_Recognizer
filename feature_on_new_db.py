import os, cv, cv2, pickle, numpy as np
from fetures_by_profilling import feature_by_projection
from features_by_box_method import feture_by_box
from feature_extraction import LCS
from MooreNeibhourTracing import moore
from feature_extraction import characters

data = {}

if __name__ == "__main__":
    fv = []
    tv = []
    os.chdir('./character-database')
    for chno in range(len(characters)):
        dstr = np.zeros((60, 40))
        size = len(os.listdir(str(chno)))
        # print size,'in',chrcs[chno]
        for ino in range(1, size + 1):
            # print str(chno) + '/' + str(ino) + '.jpg'
            dst = cv2.imread(str(chno) + '/' + str(ino) + '.jpg', 0)
            ret, dst = cv2.threshold(dst, 0, 255, cv2.THRESH_OTSU)
            l, r = 60, 40
            dst = cv2.resize(dst, (r, l))
            # dst.reshape(-1,64)
            for x in range(60):
                for y in range(40):
                    if dst[x, y] == 0:
                        dstr[x, y] += 1
            '''if dstr is None:
                dstr = feature_by_projection(dst)
            else:
                smpl = feature_by_projection(dst)
                for row in range(4):
                    lw = len(dstr[row])
                    for column in range(lw):
                        dstr[row][column] += smpl[row][column]


            # dstr = np.logical_or(dstr,feture_by_box(dst))

            #Features by moore method
            for i in range(1, l - 1):
                for j in range(1, r - 1):
                    if dst[i, j] == 0:
                        # print chrcs[chno],'-',ino
                        path = moore([i, j], dst, dst[i, j])
                        # print path,'of',chrcs[chno]
                        if len(path) > len(dstr):
                            dstr = path
                            break
                if len(dstr) > 0:
                    break
            if len(dstr) > len(data[chrcs[chno]]):
                data[chrcs[chno]] = dstr
            '''

        threshold = int(0.5 * size)
        for i in range(l):
            for j in range(r):
                if dstr[i, j] > threshold:
                    dstr[i, j] = 0
                else:
                    dstr[i, j] = 255

        data[characters[chno]] = dstr
        print np.count_nonzero(dstr), characters[chno], size
        '''for row in range(4):
            l = len(dstr[row])
            for column in range(l):
                dstr[row][column] = int(dstr[row][column]/size)
        '''

    os.chdir('..')
    # data = [fv, tv]
    file = open('pixel-new-feature.np', 'wb')
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
    file.close()
    print data
