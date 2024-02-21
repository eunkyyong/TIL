def bfs(SV, SW):
    Q = []   # Q를 만들어준다.
    Q.append((SV, SW))  # Q에 s를 채운다.
    visited = [[0] * N for _ in range(N)]  # visited 를 만든다.
    visited[SV][SW] = 1

    while Q:
        vR, vC = Q.pop(0)  # Q에서 뺀다.
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            wR = vR + dr
            wC = vC + dc

            if 0<=wR<N and 0<=wC<N:
                if G[wR][wC] == 3:
                    return visited[vR][vC]+1
                if G[wR][wC] == 0 and not visited[wR][wC]:
                    Q.append((wR, wC))
                    visited[wR][wC] = visited[vR][vC] + 1
    return 0


T = 2
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    G = [list(map(int, input())) for _ in range(N)]
    # print(G)
    for row in range(N):
        if G[row].count(2):
            SW = G[row].index(2)
            break
    SV = row
    print(f'#{tc} {bfs(SV, SW)}')
