N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
Min = 2500
# M개씩 N줄
for r in range(N-7):
    for c in range(M-7):
        cnt = 0
        board = [[0] * 8 for _ in range(8)]
        for i in range(r, r+8):
            for j in range(c, c+8):
                board[i-r][j-c] = arr[i][j]
        print(f'r:{r}, c:{c}')
        for i in range(8):
            print(*board[i])
        print()
                if arr[r][c] == 'W':
                    if (i-r)%2==0 and (j-c)%2== 1 and arr[i][j] == 'W':
                        cnt += 1
                    elif (i-r)%2==1 and (j-c)%2 == 0 and arr[i][j] == 'W':
                        cnt += 1
                    elif (i-r)%2==0 and (j-c)%2== 0 and arr[i][j] == 'B':
                        cnt += 1
                    elif (i-r)%2==1 and (j-c)%2==1 and arr[i][j] == 'B':
                        cnt += 1

                elif arr[r][c] == 'B':
                    if (i-r) % 2 == 0 and (j-c) % 2 == 1 and arr[i][j] == 'B':
                        cnt += 1
                    elif (i-r) % 2 == 1 and (j-c) % 2 == 0 and arr[i][j] == 'B':
                        cnt += 1
                    elif (i-r) % 2 == 0 and (j-c) % 2 == 0 and arr[i][j] == 'W':
                        cnt += 1
                    elif (i-r) % 2 == 1 and (j-c) % 2 == 1 and arr[i][j] == 'W':
                        cnt += 1
            # print(i, j, cnt)
        if Min > cnt:
            Min = cnt
print(Min)