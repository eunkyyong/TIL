from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = []
def bfs(y, x):
    global answer
    q=deque()
    q.append((y, x))
    num = 1
    while q:
        ny, nx = q.popleft()

        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 1:  # 범위 추가
                q.append((ny, nx))
                num += 1
                arr[ny][nx] = num
                if (ny, nx) == (N, M):
                    return num



print(bfs(1,1))



# res = 0
# for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#     xx, yy = x+dx, y+dy
#     돌면서 dfs or bfs