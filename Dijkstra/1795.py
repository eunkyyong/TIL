'''
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''
INF = int(1e7)
def dijk(now):
    U = []
    D = [INF]*(N+1)
    D[now] = 0   # 현재는 안갔으니까 가중치 0
    # 도착 노드에 도착하지 않았을 동안!!
    while X not in U:
        minV = INF
        for i in range(N+1):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i
        U.append(now)

        for i in range(N+1):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], D[now]+G[now][i])
    min_distance = len(D)
    return D[min_distance - 1]

def dijk1(X, j):
    U = []
    D = [INF]*(N+1)
    D[X] = 0  # 처음에 X가 안들어간 듯
    U.append(X)
    while j not in U:
        minV = INF
        for i in range(N+1):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                j = i
        U.append(j)

        for i in range(N+1):
            if i in U: continue
            if G[j][i]:
                D[i] = min(D[i], D[j]+G[j][i])
    min_distance = len(D)
    return D[min_distance - 1]

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    G = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        G[x][y] = c
    # print(G)
    maxV = 0
    for j in range(1, N+1):
        if j != X:
            ans = dijk(j)
            ans1 = dijk1(X, j)
            ans += ans1
            if maxV < ans:
                maxV = ans
        else:
            continue
    print(f'#{tc} {maxV}')
