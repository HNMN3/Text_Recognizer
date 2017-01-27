# Keep coding and change the world..And do not forget anything..Not Again..
from sklearn import datasets
from sklearn.externals import joblib
from skimage.feature import hog
from sklearn import svm
from sknn.mlp import Classifier, Layer
import numpy as np, os, cv2

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',',
              '-', '&', '@']

os.chdir('./character-database')
list_hog_fd = []
label = []
total = 0
for ch_no in range(len(characters)):
    dstr = None  # np.zeros((60, 40))
    size = len(os.listdir(str(ch_no)))
    total += size
    for ino in range(1, size + 1):
        dst = cv2.imread(str(ch_no) + '/' + str(ino) + '.jpg', 0)
        dst = cv2.GaussianBlur(dst, (5, 5), 0)
        ret, dst = cv2.threshold(dst, 0, 255, cv2.THRESH_OTSU)
        dst = cv2.resize(dst, (28, 28))
        dst = cv2.dilate(dst, (3, 3))
        fd = hog(dst, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1),
                 visualise=False)
        list_hog_fd.append(fd)
        label.append(characters[ch_no])
hog_label = np.array(label, 'str')
hog_features = np.array(list_hog_fd, 'float64')

nn = Classifier(
    layers=[
        Layer("Rectifier", units=100),
        Layer("Softmax")],
    learning_rate=0.03,
    n_iter=10)
nn.fit(hog_features, hog_label)
os.chdir(os.pardir)
joblib.dump(nn, "characters_nn_extended100.pkl", compress=3)
print total
