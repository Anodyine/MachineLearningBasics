import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from DecisionTree import DecisionTree
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("decisionTreeTest.data")
X = df.values[:,0:5] # select columns
# X0 = df.values[0,0:5] # select row
y = df.values[:,5] # select column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
model = DecisionTree()
model.fit(X_train, y_train)
# model.fit(X, y)

# for i in range(X.shape[0]):
#     print(model.predict(X[i,:]) == y[i])
print("Trained Results:")
for i in range(X_train.shape[0]):
    print(model.predict(X_train[i,:]) == y_train[i])
    
print("Test Results:")
for i in range(X_test.shape[0]):
    print(model.predict(X_test[i,:]) == y_test[i])
    
# df = pd.read_csv("census-income.data")
# df[['instance_weight']].plot.hist(bins=np.arange(50)*100)
# plt.show()