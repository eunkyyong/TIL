from collections import deque
def bfs(arr, N, k):
    q = deque()
    v = [[0]*N for _ in range(N)]
    q.append((y, x))
    v[0][0] = 1
    while q:
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<N and arr[ny][nx]>k:
                q.append((ny, nx))
                v[ny][nx] = v[y][x] + 1
        # 더이상 갈 수 없으면(인접한 곳 중 아무데도 갈 수 없음) 끝!
        if 모든 arr[ny][nx] <= k:
            return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = max(map(max, arr)
# 막판 도착지점이 중요하지는 않다
# 전체적으로 다음 갈 수 있는 지점을 탐색하면서 bfs
max_safety = 0
for i in range(2, Max):
    for m in range(N):
        for n in range(N):
            bfs(arr, N, k)
            cnt += 1
    if max_safety < cnt:
        max_safety = cnt
print(max_safety)
