from collections import deque
def bfs(arr, N, k):
    q = deque()
    v = [[0]*M for _ in range(N)]
    q.append((y, x))
    v[0][0] = 1
     while q:
         y, x = q.popleft()
         if (y, x) == ()

         for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
             ny, nx = y + dy, x + dx
             if 0<=ny<N and 0<=nx<M and arr[ny][nx]>k:
                q.append((ny, nx))
                v[ny][nx] = v[y][x] + 1



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = max(map(max, arr)
for k in range(2, Max+1):
    bfs(arr, N, k)
