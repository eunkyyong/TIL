def dfs(s):
    st = []
    visited = [False] * (N+1)
    st.append(s)
    visited[s] = True
    dr = [-1, 0, +1, 0]
    dc = [0, 1, 0, -1]
    route = []
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        # 0이 있는 길로..경로탐색해야 함
        while st:
            if arr[nr][nc] == 0:
                v = st.pop()
            if 0 <= nr < N and 0 <= nj < M:
                route.append(v)   # 경로 출력
            for w in G[v]:
                if not visited[w]:
                    st.append(w)
                    visited[w] = True
        if  route[-1] == 3:
            return 1
        else:
            return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            # 2에서 출발
            if arr[r][c] == 2:
                dfs(2)
                # dfs(2)!!!! 2의 4방향에 0이 있는 지 확인


            
            if arr[r][c] == 0:
                # 0이면 갈 수 있음

