# 正の整数Kが与えられた時、K以下の753数が何個あるか求めよ。
# 753数：格桁の値が7,5,3のいづれかであり、かついづれも一度は登場する整数
# ビット演算なしでやろうとして無理だったので、答え見た。。。
# pythonは引数countをlistにしないと値が更新されない。

import numpy as np

def count753(K, current, p, count):
    if current > K: return
    if p == 0b111: count[0] += 1; print(current)
    count753(K, current * 10 + 7, p | 0b001, count)
    count753(K, current * 10 + 5, p | 0b010, count)
    count753(K, current * 10 + 3, p | 0b100, count)

K = 9999
count = [0]
count753(K, 0, 0, count)
print(count)
