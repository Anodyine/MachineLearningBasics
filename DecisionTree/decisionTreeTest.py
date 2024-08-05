from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from DecisionTree import DecisionTree
import pandas as pd 

df = pd.read_csv("decisionTreeTest.data")
X = df.values[:,0:4]
y = df.values[:,5]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X)
print(y)
model = DecisionTree()
model.fit(X, y)
numSamples, numFeatures = X.shape
for i in range(numSamples):
    print(model.predict(X[i,:]) == y[i])