import sys
sys.stdin = open("/input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    # 도착지점으로부터 올라가는 중
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    lad = arr[i][j]
    i = 99
    j = 0
    # 도착지점 2인 곳부터 start
    for i in range(0, 100, -1):
        for j in range(0, 100, -1):
            if arr[i][j] == 2:
                if arr[i-1][j] == 1:  # end = arr[99][j] 도착지점~
                    row = i - di[0]  # row = 98 일 때 것 기준(99일 때 2)
                    col = j
                    # 좌우 탐색
                    if arr[i][j-1] == 1:
                        col = j - dj[1]
                    if arr[i][j + 1] == 1:
                        col = j - dj[2]
                    # 시작지점 도착할 때
                

