# recursive function
# Q. 1からNまでの総和

print("The number of integers(from 0): ")
N = int(input())

def func(N):
    # ベースケース
    if N == 0: return 0
    # 再帰呼び出し
    result = N + func(N - 1)
    return result

print(func(N))
