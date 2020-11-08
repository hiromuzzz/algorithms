# linear search method
# Q. N個の整数の中から何個か値を選んで、その総和が任意の正の整数Wになりうるか？
# ビット演算で求める。

import numpy as np

print("The number of integers(from 0): ")
N = int(input())
print("Expected total: ")
W = int(input())

a = np.arange(N)
exist = False

for bit in np.arange(1 << N):
    total = 0
    i = 0
    for v in a:
        if bit & (1 << i):
            total += v
        i += 1
    if total == W:
        exist = True
        break 

print("exist? ", exist)