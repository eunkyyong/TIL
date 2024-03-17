from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

def bfs(y, x):
    q=deque()
    v = [[0]*M for _ in range(N)]
    q.append((y, x))
    v[1][1] = 1

    while q:
        y, x = q.popleft()
        if (y, x) == (N-1, M-1):
            return v[N-1][M-1]

        for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 1:
                q.append((ny, nx))
                v[ny][nx] = v[y][x] + 1


answer = bfs(1,1)
print(answer)
#
#
#
# # res = 0
# # for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
# #     xx, yy = x+dx, y+dy
#     돌면서 dfs or bfs
# from collections import deque
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
#
# answer = []
# def bfs(y, x):
#     global answer
#     q=deque()
#     q.append((y, x))
#     num = 1
#
#     while q:
#         same_order = len(q)
#         for _ in range(same_order):
#             y, x = q.popleft()
#
#             for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 ny, nx = y + dy, x + dx
#                 if 0<=ny<N and 0<=nx<M and arr[ny][nx] != 0:
#                     num += 1
#                     q.append((ny, nx))
#                     arr[ny][nx] = num
#                     num -= 1
#                     if (ny, nx) == (N-1, M-1):
#                         return num+1
#
#                 # 모두 0이면 print할 것이 없다(이동X) num 원래대로
#
#         for n in range(N):
#             for m in range(M):
#                 if arr[n][m] == num + 1:
#                     num += 1
#
#         print(f'(y, x): {(y, x)}')
#         print(q)
#         for i in range(len(arr)):
#             print(arr[i])
#         print()
#
# answer = bfs(1,1)
# print(answer)