'''
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''
# from collections import deque
# def bfs(arr, S):
#     global resV
#     q = deque()
#     q.append(S)
#     # 노드 개수만 있음 방문 유무 기록 가능
#     visited = [0]*101
#     visited[S] = 1
#     maxV = 0
#     cnt = 0
#
#     while q:
#         now, cnt = q.popleft()
#         if maxC < cnt:
#             maxC = cnt
#             resV = now
#         elif maxC == cnt:
#             resV = max((, now))
#
#         for i in range(101):
#             if visited[i] == 0 and arr[now][i] ==  1:
#                 visited[i] = 1
#                 q.append(i)
#
#
#     return
#
# T = 10
# for tc in range(1, T+1):
# length, S = map(int, input().split())
# lst = list(map(int, input().split()))
# arr = [[0]*101 for _ in range(101)]
# for y in range(0, len(lst), 2):
#     # arr에 넣자
#     pos_y = lst[y]
#     pos_x = lst[y+1]
#     arr[pos_y][pos_x] = 1
#     bfs(arr, S)
#     print(f'#{tc} {bfs(S)}')
#########
def bfs(s):
    global resV
    Q = []
    visited = [False] * 101
    maxC = 0
    Q.append((s, 0))
    visited[s] = True

    while Q:
        v, cnt = Q.pop(0)
        if maxC < cnt:
            maxC = cnt
            resV = v
        elif maxC == cnt:
            resV = max(resV, v)

        for w in G[v]:
            if not visited[w]:
                Q.append((w, cnt +1))
                visited[w] = True
    return resV

T = 10
for tc in range(1, T+1):
    length, S = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [set() for _ in range(101)]
    for y in range(0, length, 2):
        # arr에 넣자
        v1 = lst[y]
        v2 = lst[y+1]
        G[v1].add(v2)
    resV = 0
    bfs(S)
    print(f'#{tc} {resV}')

