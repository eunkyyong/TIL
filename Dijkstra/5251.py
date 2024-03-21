INF = int(1e6)
def dijk(now):
    U = []
    D = [INF] * (V+1)
    D[now] = 0

    while len(U) < V+1:
        minV = INF
        for i in range(V+1):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        for i in range(V+1):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], D[now]+G[now][i])
    ans = len(D)
    print(D[ans-1])

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0]* (V+1) for _ in range(V+1)]

    for i in range(E):
        v1, v2, w = map(int, input().split())
        G[v1][v2] = w

    print(f'#{tc}', end = ' ')
    dijk(0)