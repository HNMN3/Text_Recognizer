import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import cv2
import os
from BoundingRect import bounding_rect
from string import ascii_letters
from ConnectedComponents import connected_components

chars = ascii_letters[-26:]+ascii_letters[:26]
target = map(str, range(10)) + list(chars)

# Following directory contains various directory
# where mapping is as follows
# 0 -> 0
# 1 -> 1
# 5 -> 5
# 9 -> 9
# A -> 10
# D ->  13
# Z -> 35
# a -> 36
# and so on
# It matches with target variable data
os.chdir('path_to_images_directory')

# Following code reshapes images in 64*64 data
# and store it as csv file for training purpose

image_data = pd.DataFrame()
for index, label in enumerate(target):
    os.chdir(str(index))

    for item in os.listdir(os.curdir):
        original_img = cv2.imread(item, cv2.IMREAD_GRAYSCALE)
        cvt_img = cv2.threshold(original_img, 0, 1, cv2.THRESH_BINARY)[1]
        cvt_img = cv2.resize(cvt_img, (64, 64))
        row = pd.Series(cvt_img.ravel())
        row['label'] = label
        image_data = image_data.append(row, ignore_index=True)
    os.chdir(os.pardir)

image_data.to_csv('input/train.csv', index=False)