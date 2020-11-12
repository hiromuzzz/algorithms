# Q. 整数K, Nが与えられる。0 <= (X, Y, Z) <= K で、 X + Y + Z = Nとなる(X,Y,Z)は何通りあるか？O(N^2)で。

import numpy as np

print("The number of integers(from 0): ")
N = int(input())
print("Expected total: ")
W = int(input())

a = np.arange(N)
exist = 0

# 0以上K以下の整数から３個選び、その総和がWとなるのは？
for bit in np.arange(1 << N):
    bin_num = bin(bit)[2:]
    count = 0
    for b in bin_num:
        count += int(b)
    total = 0
    # ２進数にしたとき、１が3個あれば、整数が３個選ばれていると言うことだから、
    if count == 3:
        i = 0
        for v in a:
            # 選んだ３つの整数の総和をとり、
            if bit & (1 << i):
                total += v
            i += 1 
    # W杜等しいくなるか？
    if total == W:
        exist += 1

print(exist)
