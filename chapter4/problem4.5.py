# 正の整数Kが与えられた時、K以下の753数が何個あるか求めよ。
# 753数：格桁の値が7,5,3のいづれかであり、かついづれも一度は登場する整数
# オーダーを無視した場合
import numpy as np

K = 9999

def count753(K):
    # 7,5,3がいづれも一度は登場するから、少なくとも３桁
    # 753数の最小値は357
    if len(str(K)) < 3 or K < 357: return 0
    # 偶数は除く
    Ks = np.arange(357, K + 1 , 2)
    count = 0
    for i in Ks:
        seven = 0
        five = 0
        three = 0
        pre = 0
        tmp = 0
        # 各桁を分解して、それぞれが753か調べる。
        for j in list(str(i)):
            save = pre
            if j == '7':
                seven += 1
                pre += 1
            elif j == '5':
                five += 1
                pre += 1
            elif j == '3':
                three += 1
                pre += 1
            else:
                tmp = 0
                break
            if seven >0 and five > 0 and three > 0 and pre > save:
                tmp += 1
        count += tmp
    return count

print(count753(K))
        
