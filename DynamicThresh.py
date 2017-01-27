# Keep Coding And change the world and do not forget anything... Not Again..
import cv, numpy, cv2


def D_ThreshBinary(image):
    l, r = image.shape[:2]
    h = 2
    w = int(r / 64)
    Tmin = 50
    TFixed = 0
    for i in range(0, l - h, h):
        for j in range(0, r - w, w):
            img = image[i:i + h, j:j + w]
            hist = cv.calcHist([img], [0], None, [256], [0, 256])
            flag = 0
            for item in hist:
                if item[0] > 0:
                    break
                flag += 1

            if flag > Tmin:
                var = cv.meanStdDev(img)
                var = int(var[1][0] ** 2)
                dthres = (((flag - Tmin) - min(TFixed, flag - Tmin)) * 2)
                if var < dthres:
                    image[i:i + h, j:j + w] = 255
                else:
                    image[i:i + h, j:j + w] = 0
            else:
                image[i:i + h, j:j + w] = 0
    return image


if __name__ == "__main__":
    img = cv2.imread('sample_check.jpg', 0)
    cv2.imwrite('threash_checking.jpg', D_ThreshBinary(img))
    print("done")
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
