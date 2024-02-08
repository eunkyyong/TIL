T = int(input())
V, E = map(int, input().split())
M = [[] for _ in range(V+1)]  #
for _ in range(E):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
