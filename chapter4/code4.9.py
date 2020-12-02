# recursive function
# Q. 部分和問題（例えば、１０個の連続する整数から何個か選んだ総和が20になるか？）
import numpy as np

def func(i, W, a):
    # ベースケース
    if i == 0:
        if W == 0:
            return True
        else:
            return False
    # a[i-1]を選ばない場合
    if func(i-1, W, a): return True
    # a[i-1]を選ぶ場合
    if func(i-1, W-a[i-1], a): return True
    # どちらもfalseならfalse
    return False

N = 10
W = 20
a = np.arange(N)

print(func(N, W, a))






