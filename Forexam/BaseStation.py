T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n+1)]
    cnt = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for a in range(4):
                    if 0<=i+dx[a]<n and 0 <= j + dy[a] < n:
                        arr[i+dx[a]][j+dy[a]] = 'X'

            elif arr[i][j] == 'B':
                for c in range(4):
                    for p in range(1, 3):
                        if 0 <= i + dx[c]*p < n and 0 <= j + dy[c]*p < n:
                            arr[i+dx[c]*p][j+dy[c]*p] = 'X'

            elif arr[i][j] == 'C':
                for e in range(4):
                    for q in range(1, 4):
                        if 0 <= i + dx[e]*q < n and 0 <= j + dy[e]*q < n:
                            arr[i+dx[e]*q][j+dy[e]*q] = 'X'
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')