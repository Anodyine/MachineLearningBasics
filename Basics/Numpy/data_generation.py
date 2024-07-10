import numpy as np

print('np.zeros((2,3))')
print(np.zeros((2,3)))

print('np.ones((2,3))')
print(np.ones((2,3)))

print('10*np.ones((2,3))')
print(10*np.ones((2,3)))

print('np.eye(3)')
print(np.eye(3))

print('np.random.random()')
print(np.random.random())

print('np.random.random((2,3))')
print(np.random.random((2,3)))

print('np.random.randn(2,3)') # randn does not take a tuple!!!!
print(np.random.randn(2,3))

print('R = np.random.randn(10000)')
R = np.random.randn(10000)
print(R)

print('R.mean()')
print(R.mean())

print('R.var()')
print(R.var())

print('R.std()')
print(R.std())

print('R = np.random.randn(10000, 3)')
R = np.random.randn(10000, 3)
print(R)

print('R.mean(axis=0)')
print(R.mean(axis=0))

print('R.mean(axis=1)')
print(R.mean(axis=1))

print('R.mean(axis=1).shape')
print(R.mean(axis=1).shape)

print('np.cov(R).shape') 
print(np.cov(R).shape) # this proves that numpy expects each column to be a sample

print('np.cov(R.T).shape') 
print(np.cov(R.T).shape) # this is the way to handle things if each row is a sample. We have 3 variables that have 10000 measurements each and are finding the cov between them

print('np.cov(R, rowvar=False).shape') 
print(np.cov(R, rowvar=False).shape) # or this

print('np.cov(R, rowvar=False)') 
print(np.cov(R, rowvar=False)) # or this

print('np.random.randint(0, 10, size=(3,3))') 
print(np.random.randint(0, 10, size=(3,3))) 

print('np.random.choice(10, size=(3,3))')
print(np.random.choice(10, size=(3,3)))

print('np.linspace(0, 20, 1000)')
print(np.linspace(0, 20, 10))
