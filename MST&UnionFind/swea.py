INF = int(1e6)
def prim(now):
    U = []
    D = [INF] * (V+1)
    D[now] = 0

    while len(U) < V+1:
        # D에 저장된 것 중 제일 작은 값인 vertex를 고른다.
        # 단, 아직 안가본 것 중
        minV = INF
        for i in range(V+1):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        # now와 연결된 vertex들의 값을 최소로 update
        for i in range(V+1):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], G[now][i])
                # print(f'{now}, {i}번째 최솟값 {D}')

    print(sum(D))
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        v1, v2, w = map(int, input().split())
        G[v1][v2] = w
        G[v2][v1] = w
    # print(G)

    print(f'#{tc}', end = ' ')
    prim(0)