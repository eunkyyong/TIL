# import sys
# sys.stdin = open("C:\cek\PycharmProjects\pythonProject\Today-I-Learned\input2.txt","r")

def chg(N): #chargeN
    chLoc = 0 #chargeLocation
    chP = 0 # index
    cnt = 0
    for i in range(K):
        for j in range(1, M):
            if i*(N//K) < lst[j]:
                chLoc = lst[j-1]
                chP = j
                cnt += 1
    if cnt == 0:
        return cnt
    return cnt


T = int(input())
for i in range(T):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{i+1} {chg(N)}')