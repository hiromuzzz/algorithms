# linear search method
# Q. N個の整数が与えられ、「値が全て偶数だったら、全て２で割った値に置き換える」という操作を何回行えるかを求める。

import numpy as np

# サンプルデータ
# 全部偶数の場合
N = [6,8,10,100,50] 
# 奇数が混ざっている場合
# N = [3,4,6,8,9]

min_val = N[0]

# 各値を２で割った値の最小値が、与えられた数列に対して、問題の操作を行える回数（0は例外）。
# ただし、一つでも奇数が混ざっていれば、一回も操作は行えない。
for v in N:
    if v != 0 and v % 2 == 0 and v / 2 < min_val:
        min_val = v / 2
    if v % 2 != 0:
        min_val = 0
        break

print(int(min_val))
