# Keep Coding And change the world and do not forget anything... Not Again..
import cv2


def dynamic_threshing(image):
    '''
    This method converts the image into binary where foreground components are represented
    with black(0) pixels and background is represented with white(255) pixel
    :param image: input image
    :return: converted image
    '''
    l, r = image.shape[:2]
    h = 2
    w = int(r / 64)
    t_min = 50
    t_fixed = 0
    for i in range(0, l - h, h):
        for j in range(0, r - w, w):
            img = image[i:i + h, j:j + w]
            hist = cv2.calcHist([img], [0], None, [256], [0, 256])
            min_intensity = 0
            for item in hist:
                if item[0] > 0:
                    break
                min_intensity += 1

            if min_intensity > t_min:
                var = cv2.meanStdDev(img)
                var = int(var[1][0] ** 2)
                dthres = ((min_intensity - t_min) - min(t_fixed, min_intensity - t_min)) * 2
                if var < dthres:
                    image[i:i + h, j:j + w] = 255
                else:
                    image[i:i + h, j:j + w] = 0
            else:
                image[i:i + h, j:j + w] = 0
    return image


if __name__ == "__main__":
    img = cv2.imread('sample_check.jpg', 0)
    cv2.imwrite('threash_test.jpg', dynamic_threshing(img))
