def dfs(s):
    st = []
    visited = [False] * (node+1)
    st.append(s)
    visited[s] = True

    while st:
        v = st.pop()
        # v의 개수가 답임

        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = int(N//10)
    G = [[] for _ in range(node+1)]
    for i in range(node//2+1, node+1, 2):  # 간선 개수 범위에 따라


    print(f'#{tc}', )