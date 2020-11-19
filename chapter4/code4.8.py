# recursive function
# Q. フィボナッチ数列

import numpy as np

def fibo(N):
    # ベースケース
    # 書籍の中ではreturnされているが、memoしておかないと数列の初めの2つの値が-1のままになってしまう。
    # returnは15行目がその役割を担う。
    if N == 0: 
        memo[N] = 0
    elif N == 1:
        memo[N] = 1
    
    if memo[N] != -1: return memo[N]

    # 再帰呼び出し
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

memo = []
# 値が５０個の配列
memo = np.arange(50)
# -1で初期化
memo[:] = -1
# フィボナッチ数列を求める
fibo(49)
print(memo)





