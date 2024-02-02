import sys
sys.stdin = open("C:\cek\pycharm\TIL\input (5).txt","r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    N += 1 # 0인 행과 열 추가
    # 가로, 세로로 연속한 1 의 개수가 K 인
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt += 1
        else:  # arr[i][j]==0이면 (0이 아니면 참)
            if cnt == K:
                ans += 1
            cnt = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else:  # arr[i][j]==0이면
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f'#{tc} {ans}')