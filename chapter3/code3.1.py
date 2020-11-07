# linear search method
# Q. For integer a0...aN-1 and v, is there any data where ai = v ? 

import numpy as np

print("The number of integers(from 0): ")
N = int(input())
print("A value to compare(integer): ")
v = int(input())

exist = False

for i in np.arange(N):
    if i == v:
        exist = True

print(exist)
