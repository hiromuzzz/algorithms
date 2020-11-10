# linear search method
# Q. N個の整数から２個選び、その差の最大値を求める。O(N)で。

import numpy as np

print("The number of integers(from 0): ")
N = int(input())

a = np.arange(N)
a = [10,3,4,6,8,100,29]
max_val = a[0]
min_val = a[0]

for v in a:
    if v < min_val:
        min_val = v 
    if v > max_val:
        max_val = v

# 差の最大値は、N個の整数の最小値と最大値との差だから、
diff = max_val - min_val

print("max diff value: ", diff)

