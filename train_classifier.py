# Keep Coding And change the world and do not forget anything... Not Again..
from string import ascii_letters

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns

warnings.filterwarnings('ignore')
sns.set()

train = pd.read_csv('input/train_transformed.csv')

# Split the data into independent and dependent variable
X = train.copy()
y = X.pop('label')

# Split the training data into training and testing set to see how
# it works on unseen data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Let's try some simple model first
from sklearn.naive_bayes import GaussianNB

model_name = "Gaussian Naive Bayes"
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

chars = ascii_letters[-26:] + ascii_letters[:26]
target = map(str, range(10)) + list(chars)

# Check the model performance
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cm, index=list(target), columns=list(target))

for start, end, title in [('0', '9', 'digits'), ('A', 'Z', 'letters'), ('a', 'z', 'letters')]:
    plt.figure(figsize=(9, 9))
    sns.heatmap(df_cm.loc[start:end, start:end], square=True, annot=True)
    plt.title(title)
    plt.ylabel('Actual Value')
    plt.xlabel('Predicted Value')

cm_accuracy = np.sum(df_cm.loc[item, item] for item in target) * 1.0 / np.ravel(df_cm).sum()
print(cm_accuracy)  # 0.143965851766

# Let's check the accuracy with cross validation
from sklearn.model_selection import cross_val_score

cv_score = cross_val_score(model, X, y, cv=7)
print(np.average(cv_score))  # 0.152931486178 # this model is giving only 15% accuracy

# Let's plot the learning curve
from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(model, X, y)
train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
plt.plot(train_sizes, train_scores_mean, '.-', c='r', label='Training score')
plt.plot(train_sizes, test_scores_mean, '.-', c='g', label='Cross validation score')
plt.legend(loc='best')
plt.title('Learning Curves({})'.format(model_name))
plt.xlabel('Training examples')
plt.ylabel('Score')

# Let's Check SVM classifier
from sklearn.svm import SVC

model = SVC()
# Let's tune the hyperparameters `kernel` and `C` with GridSearchCV
from sklearn.model_selection import GridSearchCV

grid_params = {'kernel': ['linear', 'rbf'], 'C': [1, 2, 4, 8]}
grid = GridSearchCV(model, grid_params)

grid.fit(X, y)
print(grid.best_params_)  # {'C': 8, 'kernel': 'rbf'}

model = grid.best_estimator_
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Check the model performance
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

# our test data doesn't contains all the labels so let's remove those
outlier = []
for label in target:
    if (y_test == label).sum() == 0:
        outlier.append(label)
for item in outlier:
    target.remove(item)

# convert ndarray in DataFrame
df_cm = pd.DataFrame(cm, index=list(target), columns=list(target))

for start, end, title in [('0', '9', 'digits'), ('A', 'Z', 'letters'), ('a', 'z', 'letters')]:
    plt.figure(figsize=(9, 9))
    sns.heatmap(df_cm.loc[start:end, start:end], square=True, annot=True)
    plt.title(title)
    plt.ylabel('Actual Value')
    plt.xlabel('Predicted Value')

cm_accuracy = np.sum(df_cm.loc[item, item] for item in target) * 1.0 / np.ravel(df_cm).sum()
print(cm_accuracy)
# out: 0.863795110594 # SVM is working very nice on this
# but cross validation is the right way to check accuracy

# Let's check the accuracy with cross validation
from sklearn.model_selection import cross_val_score

cv_score = cross_val_score(model, X, y, cv=7)
print(np.average(cv_score))  # 0.860399036 # this model is giving very good accuracy of 86%

# Let's train the classifier on complete data and save it using pickle
from sklearn.externals import joblib

model.fit(X, y)

# save classier
with open('pickle_objects/classifier.pkl', 'wb') as classifier_file:
    joblib.dump(model, classifier_file)
