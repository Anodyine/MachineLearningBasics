import numpy as np

a = np.array([1,2])
b = np.array([3,4])

dot = 0
# Non-pythonic
for idx, e in enumerate(a):
    dot += e*b[idx]
print(dot)

dot = 0
# Non-pythonic
for i in range(len(a)):
    dot += a[i]*b[i]
print(dot)

dot = 0
# Use zip
for e, f in zip(a,b):
    dot += e*f
print(dot)
    
dot = 0
dot = np.sum(a*b)
print(dot)

print((a*b).sum())
print(np.dot(a,b))
print(a.dot(b))
print(a@b)

print('amag =')
print(np.sqrt((a*a).sum()))
print(np.linalg.norm(a))
print('cosangle =')
print(a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b)))
print('angle between a and b(rad) =')
print(np.arccos(a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))))
print('angle(deg) =')
print(180*(np.arccos(a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))))/np.pi)