# linear search method
# Q. 2個以上のN個の整数の中から２番目に小さいを求める。O(N)で。

import numpy as np

print("The number of integers(from 0): ")
N = int(input())

a = np.arange(N)

# 以下のアルゴリズムは、最小値と２番目に小さい値の初期値を十分大きな値にしておかないとうまくいかない
# 例えば初期値０では両方０が出力される
# min_val = 0
# min_val2 = 0
min_val = 99999
min_val2 = 99999

for v in a:
    if v < min_val:
        min_val2 = min_val
        min_val = v
    elif v < min_val2:
        min_val2 = v

print("minimum value: ", min_val)
print("2nd minimum value: ", min_val2)


# 以下のようにO(2N)であれば、初期値によらず２番目に小さい値を求めることができるが。。。

for v in a:
    if v < min_val:
        min_val = v
# 与えられる数が整数なので、最小値と２番目に小さい値との差は少なくとも1
diff_val = 1
for v in a:
    if diff_val >= v - min_val and min_val != v:
        min_val2 = v

print("new 2nd minimum value: ", min_val2)

