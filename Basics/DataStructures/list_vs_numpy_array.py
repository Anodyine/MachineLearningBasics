import numpy as np

L = [1, 2, 3]

print('Lists:')
print('L = [1, 2, 3]')
for e in L:
    print(e)
    
L2 = L.copy()
L2.append(4)

print('L.append(4) = ')
for e in L2:
    print(e)

print('L + [5] = ')
for e in L + [5]:
    print(e)
    
print('2 * L = ')
for e in 2 * L:
    print(e)
    
print('L + L = ')
for e in L + L:
    print(e)
    
print('Square bracket lambda: [e + 3 for e in L] = ')
for e in [e + 3 for e in L]:
    print(e)
    
A = np.array([1, 2, 3])

print('Arrays:')
print('A = np.array([1, 2, 3])')
for e in L:
    print(e)
     
print('Broadcasting: A + np.array[4]')
for e in A + np.array([4]):
    print(e)

print('Elementwise: A + np.array[4,5,6]')
for e in A + np.array([4,5,6]):
    print(e)

print('Will cause dimension error: A + np.array[4,5]')

print('Elementwise: 2*A')
for e in 2*A:
    print(e)

print('Elementwise: A**2')
for e in A**2:
    print(e)

print('Elementwise: np.tanh(A)')
for e in np.tanh(A):
    print(e)
