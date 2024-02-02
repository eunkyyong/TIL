# 목표지점을 먼저 찾아라!!!
import sys
sys.stdin = open("C:\cek\pycharm\input.txt","r")

T = 10 # 확인하기 위해
for _ in range(1, T+1):
    N = 100
    tc = int(input())
    LADDER = [list(map(int, input().split())) for _ in range(N)]
    # print(f'#{tc} {LADDER}')

    #1. 99번째 row에서 2의 위치를 찾아라.
    for col in range(N):
        if LADDER[99][col]  == 2:
            break
    # print(col)
    #2. 위로 한칸씩 이동하면서
    for row in range(98, -1, -1): # range도 거꾸로 써야하는구낭!!
        #2-1. col의 왼쪽에 1이 있는 지 확인
        if col>0 and LADDER[row][col-1] == 1:
            while col>0 and LADDER[row][col-1] == 1:
                col -= 1
        #2-2. col의 오른쪽에 1이 있는 지 확인
        elif col<N-1 and LADDER[row][col+1] == 1:
            while col<N-1 and LADDER[row][col-1] == 1:
                col += 1
    print(col)


