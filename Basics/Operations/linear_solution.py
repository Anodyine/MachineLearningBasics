import numpy as np

# The admission fee at a small fair is $1.50 for children and $4.00 for adults. On a certain day, 2200 people enter the 
# fair and $5050 is collected. How many children and how many adults attended?

# x + y = 2200
# 1.5x + 4y = 5050
# Ax = b => x = A^-1b
# x = [x y]
# A = [1 1]
#     [1.5 4]
# b = [2200 5050]



A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])

#Using the formula:
print(np.linalg.inv(A).dot(b))

#Better because of performance:
print(np.linalg.solve(A, b))