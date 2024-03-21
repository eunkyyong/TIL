# visited 안쓰는 BFS
# [N-1][N-1]의 최소값을 return
def solve():
    INF = int(1e6)
    D = [[INF] * N for _ in range(N)]
    D[0][0] = 0
    Q = [(0, 0)]
    while Q:
        row, col = Q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc <N:
                # 음수일 때 처리
                h = max(1, arr[nr][nc]-arr[row][col]+1) 
                if D[nr][nc] > D[row][col]+h:
                    D[nr][nc] = D[row][col] + h
                    Q.append((nr, nc))
    return D[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {solve()}')