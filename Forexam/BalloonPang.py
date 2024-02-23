'''
3
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2
5 5
3 4 1 2 3
3 4 1 3 2
2 3 2 4 1
1 4 4 1 3
2 2 3 4 4
5 8
1 3 4 4 4 4 3 3
4 1 2 4 3 1 4 4
4 1 4 4 1 4 2 1
3 2 4 2 1 1 2 1
4 4 1 4 4 2 2 2
'''
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    for r in range(N):
        for c in range(M):
            leaf = arr[r][c]
            Sum = leaf
            for i in range(1, leaf+1):
                for j in range(4):
                    nr = r + i*dr[j]
                    nc = c + i*dc[j]
                    if 0<=nr<N and 0<=nc<M:
                        Sum += arr[nr][nc]
            if Max < Sum:
                Max = Sum
    print(f'#{tc} {Max}')