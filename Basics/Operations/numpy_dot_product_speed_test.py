import numpy as np
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

def for_loop_dot_product(a, b):
	result = 0
	for e, f in zip(a, b):
		result += e*f
	return result

t0 = datetime.now()
for t in range(T):
	for_loop_dot_product(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
	a.dot(b)
dt2 = datetime.now() - t0

print("Numpy dot product is:", np.round(dt1.total_seconds() / dt2.total_seconds(), 2), "times faster than a for loop dot product.")