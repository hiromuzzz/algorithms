# Q. 1~9の整数のみで作られた長さNの文字列Sが与えられる時、文字の間に＋を入れた時の総和を求める。
# ex) "125" = (1+2+5) + (1+25) + (12+5) + 125 = 176

import numpy as np

print("The number of integers(from 0): ")
S = input()

total = 0

# ＋の位置をbit演算する
plus = len(S) - 1
for p in np.arange(1 << plus):
    plus_position = list(bin(p)[2:])
    plus_position.reverse()
    index = [i for i, x in enumerate(plus_position) if x == '1']
    print(index)
    if not index:
        # ＋がない時
        total += int(S)
    else:
        start = 0
        # ＋がはいる場所で分割
        for i in index:
            # ＋より手前を足す
            total += int(S[start:i+1])
            start = i + 1
        # 最後の＋より後ろに残っている値を足す
        total += int(S[start:])

print(total)
