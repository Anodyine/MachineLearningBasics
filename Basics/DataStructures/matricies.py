import numpy as np

# List Matrix
L = [[1,2],[3,4]]

print('L = ')
for e in L:
    print(e)
    
print('L[0][1] = ')
print(L[0][1])

# Numpay Array Matrix
A = np.array([[1,2],[3,4]])

print('A = ')
for e in A:
    print(e)

print('A[0][1] = ')
print(A[0][1])

print('A[:,0] = ')
print(A[:,0])

print('A.T = ')
print(A.T)

B = np.array(
    [[1,2,3],
     [4,5,6]]
)

print('A dot B')
print(A.dot(B))

# print(B.dot(A)) is impossible because A[2][0] is undefined!

print('np.linalg.det(A) =')
print(np.linalg.det(A))

print('np.linalg.inv(A) =')
print(np.linalg.inv(A))

print('np.trace(A) =')
print(np.trace(A))

print('np.diag(A) =')
print(np.diag(A))

print('np.diag(np.diag(A)) =')
print(np.diag(np.diag(A)))

print('np.linalg.eig(A) =')
print(np.linalg.eig(A))

Lam, V = np.linalg.eig(A)
print('Lam, V = np.linalg.eig(A)')

print('Lam (eigenvalues) = ')
print(Lam)

print('V (eigenvector) = ')
print(V)

print('V[:,0] * Lam[0] = ')
print(V[:,0] * Lam[0])

print('A @ V[:, 0] = ')
print(A @ V[:,0])

print('V[:,0] * Lam[0] == A @ V[:, 0]')
print(V[:,0] * Lam[0] == A @ V[:, 0])
print('Because of numerical precision!')

print('np.allclose(V[:,0] * Lam[0], A @ V[:, 0])')
print(np.allclose(V[:,0] * Lam[0], A @ V[:, 0]))