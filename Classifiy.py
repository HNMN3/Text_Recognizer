# Keep Coding And change the world and do not forget anything... Not Again..
import argparse

from sklearn.externals import joblib
import cv2


class Classifier:
    def __init__(self):
        # Load classifier and PCA object
        with open('pickle_objects/decomposer.pkl', 'rb') as decomposer_file:
            self.pca_decomposer = joblib.load(decomposer_file)
        with open('pickle_objects/classifier.pkl', 'rb') as classifier_file:
            self.classifier = joblib.load(classifier_file)

    def predict(self, img):
        # reshape image and make it binary
        reshaped_img = cv2.resize(img, (64, 64))
        ret, cvt_img = cv2.threshold(reshaped_img, 0, 1, cv2.THRESH_OTSU)

        num_zeros = (cvt_img == 0).sum()
        num_ones = (cvt_img == 1).sum()
        if num_zeros > num_ones:
            ret, ds = cv2.threshold(reshaped_img, 0, 1, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

        # Extract features with PCA dimensionality reduction
        X_new = self.pca_decomposer.transform([cvt_img.ravel(), ])

        # predict the label
        y_new = self.classifier.predict(X_new)
        return y_new[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path',
                        help="Path of an Image")
    args = parser.parse_args()
    clf = Classifier()
    img = cv2.imread(args.image_path, 0)
    print(clf.predict(img))
