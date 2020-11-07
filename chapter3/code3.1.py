# linear search method
# Q. For integer a[0]...a[N-1] and v, is there any data where a[i] = v ? 

import numpy as np

print("The number of integers(from 0): ")
N = int(input())
print("A value to compare(integer): ")
v = int(input())

exist = False

for a in np.arange(N):
    if a == v:
        exist = True

print(exist)
