# linear search method
# Q. N個の整数の中に、任意の整数vと等しい値があるか？

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
