# linear search method
# Q. Find minimum value in the array.

import numpy as np

print("The number of integers(from 0): ")
N = int(input())

a = np.arange(N)
min_val = a[0]

for v in a:
    if min_val > v:
        min_val = v

print("minimum", min_val)