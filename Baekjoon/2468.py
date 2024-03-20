from collections import deque
def bfs(arr, N, k, y, x):
    q = deque()
    v = [[0]*N for _ in range(N)]
    q.append((y, x))

    v[y][x] = 1
    while q:
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<N and arr[ny][nx]>k and v[ny][nx]==0:
                q.append((ny, nx))
                v[ny][nx] = 1
        # 더이상 갈 수 없으면(인접한 곳 중 아무데도 갈 수 없음) 끝!
        # 다 돌고 나서 전과 값이 같으면
        if 0<y<N-1 and 0<x<N-1 and v[y+1][x] == v[y][x] and v[y-1][x] == v[y][x] and v[y][x+1] == v[y][x] and v[y][x-1] == v[y][x]:
            return (y, x)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = max(map(max, arr))
# 막판 도착지점이 중요하지는 않다
# 전체적으로 다음 갈 수 있는 지점을 탐색하면서 bfs
max_safety = 0
for i in range(2, Max):
    cnt = 0
    # (y, x) 값 바뀜.
    # for m in range(N):
    #     for n in range(N):
    #         if visited[][] == 0 and arr[m][n] > i:
    #             bfs(arr, N, i, m, n)
    #             cnt += 1
    print(f'#{i}초과 안전영역 {cnt}')
    if max_safety < cnt:
        max_safety = cnt
print(max_safety)
