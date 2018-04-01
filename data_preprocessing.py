# Keep Coding And change the world and do not forget anything... Not Again..
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from string import ascii_letters
import seaborn as sns

warnings.filterwarnings('ignore')
sns.set()

train = pd.read_csv('input/train.csv')

# Separating dependent and independent variables
X = train.copy()
y = X.pop('label')

chars = ascii_letters[-26:] + ascii_letters[:26]
target = map(str, range(10)) + list(chars)

# Visualizing data
from sklearn.decomposition import PCA

decomposer = PCA(n_components=2, svd_solver='randomized')
X_decomposed = decomposer.fit_transform(X)

plt.scatter(X_decomposed[:, 0], X_decomposed[:, 1],
            c=y.map({item: i for i, item in enumerate(target)}),
            cmap='rainbow',
            s=7)
plt.colorbar()
plt.xlabel("Principle Component 1")
plt.ylabel("Principle Component 2")
plt.title("Data Visualization")

# Looking for how many features are important
from sklearn.decomposition import PCA

pca = PCA().fit(X)
data_importance = np.cumsum(pca.explained_variance_ratio_)
plt.plot(data_importance)
plt.xlabel("Number of components")
plt.ylabel("Variance")
plt.title("PCA Variance Visualization")
# the plot shows that we can maintain >99% variance of data by using only 2500 features

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
