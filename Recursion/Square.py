def dfs(row, col):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newR = row + dr
        newC = col + dc
        if 0 <= newR < N and 0 <= newC < N and ROOM[newR][newC] == ROOM[row][col] + 1:
            if DIS[newR][newC] == 0:
                DIS[newR][newC] = dfs(newR, newC)
            return DIS[newR][newC] + 1

    return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ROOM = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    roomno = N * N
    DIS = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if DIS[row][col] == 0:
                DIS[row][col] = dfs(row, col)
                if DIS[row][col] > maxV:
                    maxV = DIS[row][col]
                    roomno = ROOM[row][col]
                elif DIS[row][col] == maxV:
                    roomno = min(roomno, ROOM[row][col])
    print(f'#{tc} {roomno} {maxV}')