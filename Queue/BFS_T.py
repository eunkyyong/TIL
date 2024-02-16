# def dfs(s):
#     ST = []
#     visited = [False] * (N+1)
#
#     ST.append(s)
#     while ST:
#         v = ST.pop(-1)
#         if not visited[v]:
#             print(v)
#             visited[v] = True
#
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#
# def bfs(s):
#     Q = []
#     visited= [False] * (N+1)     # 0번 노드 잊지 말고! 사용안하는 것 뿐?
#     Q.append(s)
#     visited[s] = 1
#     while Q:
#         v = Q.pop(0)
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = 1 + visited[v]
#
#
#
# N, E = map(int, input().split())
# lst = list(map(int, input().split()))
#
# G = [[] for _ in range(N+1)]
# for i in range(0, len(lst), 2):
#     v1 = lst[i]
#     v2 = lst[i+1]
#     G[v1].append(v2)
#     G[v2].append(v1)
#
# #
# def bfs(s):
#     Q = []
#     visited = [0] * (N+1)
#
#     Q.append(s)
#     visited[s] = True
#     while Q:
#         v, d = Q.pop(0)
#         print(v, d)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append((w, d+1))
#                 visited[w] = True
# bfs(0)
# #
def bfs(s):
    Q = []
    visited = [0] * (N+1)

    Q.append((s, 1))
    visited[s] = True
    while Q:
        v, d = Q.pop(0)
        print(v, d)

        for w in range(N+1):
            if G[v][w]==1 and not visited[w]:
                Q.append((w, d+1))
                visited[w] = True


N, E = map(int, input().split())
lst = list(map(int, input().split()))

# G = [[] for _ in range(N+1)]
'''
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
'''
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1][v2] = 1
    G[v2][v1] = 1

# print(G)
bfs(1)