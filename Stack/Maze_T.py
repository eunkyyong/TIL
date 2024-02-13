# N = 5
# s = '1 2 1 3 3 4 4 5 4 2'
# lst = list(map(int, s.split()))


# visited 가 필요하까? 안쓰고 가면서 0->1로 채우면서 가도됨!
def dfs(stR, stC):
    ST = []
    visited = [[False] * N for _ in range(N)]

    ST.append((stR, stC))  # tuple로 묶어줌
    visited[stR][stC] = True  # visited도 2dimensional
    while ST:
        vR, vC = ST.pop()
        # print(v)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR = vR + dr
            newC = vC + dc
            # 0인 지, 범위 내인지
            if 0<= newR < N and 0<= newC < N and arr[newR][newC] != 1 and not visited[newR][newC]:
            # 범위 비교 후 좌표 값 비교
                ST.append((newR, newC))
                visited[newR][newC] = True
                if arr[newR][newC] == 3:  # 안왔던 이유....
                    return 1
                ST.append((newR, newC))
                  # ST에 뭐넣기로 했지?? 여기가 문제....

    return 0

# print(lst, G)
# for i in range(0, len(lst), 2):
#     v1 = lst[i]
#     v2 = lst[i+1]
#     G[v1].append(v2)
#     G[v2].append(v1)
# G = [[] for _ in range(N+1)]
# print(G)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # for r in range(N):
    #     for c in range(N):
    #         if arr[r][c] == 2:
    #             stR = r
    #             stC = c
    #             break
    for row in range(N):
        if arr[row].count(2):
            stC = arr[row].index(2)
            stR = row
            break
    # print(arr)
    # print(stR, stC)
    print(f'#{tc}', dfs(stR, stC))