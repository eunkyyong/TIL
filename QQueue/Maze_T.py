# def bfs(s):
#     Q = []
#     visited = [False] * (N+1)
#
#     Q.append(s)
#     visited[s] = True
#     while Q:
#         v = Q.pop(0)
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = True
def bfs(stR, stC):
    Q = []
    visited = [[0] * N for _ in range(N)]

    Q.append((stR, stC))
    visited[stR][stC] = 1

    while Q:
        # v = Q.pop()
        # vR = v[0]
        # vC = v[1]
        vR, vC = Q.pop(0)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            wR = vR + dr
            wC = vC + dc

            # 영역 비교
            if 0<=wR<N and 0<=wC<N:
                if arr[wR][wC] == 3:
                    # for row in visited:
                    #     print(row)
                    return visited[vR][vC]+1

                if arr[wR][wC] == 0 and not visited[wR][wC]:
                    Q.append((wR, wC))
                    visited[wR][wC] = visited[vR][vC]+1

    return 0


T = 2
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]

    # for row in range(N):
    #     for col in range(N):
    #         if arr[row][col] == 2:
    #             stR = row
    #             stC = col
    #             break
    for row in range(N):
        if arr[row].count(2):
            stC = arr[row].index(2)
            break
    stR = row
    print(f'#{tc} {bfs(stR, stC)}')
    # print(stR, stC)