import sys
sys.stdin = open("C:\cek\pycharm\TIL\Forexam\input (12).txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 초기화 틀리지 말자.....
    Max = 0
    for r in range(0, N-M+1):
        for c in range(0, N-M+1):
            Sum = 0
            for i in range(M):
                for j in range(M):
                    Sum += arr[r+i][c+j]
            if Max < Sum:
                Max = Sum
    print(f'#{tc} {Max}')
