'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(arr)

    narr = [[0]*3 for _ in range(N)]
    for o in range(0, N):
        narr[o][0] = arr[o].count('W')
        narr[o][1] = arr[o].count('B')
        narr[o][2] = arr[o].count('R')
    print(narr)

    Min = 1000
    for l1 in range(1, N-1):
        for l2 in range(2, N):
            if l1<l2:
                Sum = 0
                for i in range(0, l1):
                    Sum += narr[i][1] + narr[i][2]
                for j in range(l1, l2):
                    Sum += narr[j][0] + narr[j][2]
                for k in range(l2, N):
                    Sum += narr[k][0] + narr[k][1]

                if Min > Sum:
                    Min = Sum
    print(f'#{tc} {Min}')