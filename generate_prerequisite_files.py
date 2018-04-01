# Keep Coding And change the world and do not forget anything... Not Again..
import pandas as pd
import os

# confirm required directory exists

if not os.path.exists('input'):
    os.mkdir('input')
if not os.path.exists('pickle_objects'):
    os.mkdir('pickle_objects')

# make train.csv from images
import make_training_data

# make train_transformed.csv with PCA
train = pd.read_csv('input/train.csv')
X = train.copy()
y = X.pop('label')

from sklearn.decomposition import PCA

pca = PCA(n_components=2500)
X_transformed = pca.fit_transform(X)

# Save pca ob
from sklearn.externals import joblib

with open('pickle_objects/decomposer.pkl', 'wb') as decomposer_file:
    joblib.dump(pca, decomposer_file)

train_transformed = pd.DataFrame(X_transformed)
train_transformed['label'] = y

# save transformed data
train_transformed.to_csv('input/train_transformed.csv', index=False)

from sklearn.svm import SVC

model = SVC(C=8, kernel='rbf')
model.fit(X, y)

# save classier
with open('pickle_objects/classifier.pkl', 'wb') as classifier_file:
    joblib.dump(model, classifier_file)
