# import sys
# sys.stdin = open("/Users/eunkyyong/PycharmProjects/pythonProject/TIL/Stack/sample_input.txt", "r")
def dfs(s):
    st = []
    visited = [False] * (V+1)
    st.append(s)
    visited[s] = True  # 1이라는 소린가?

    while st:
        v = st.pop()
        # print(v)
        # S, G 출발, 도착점이 찍히면 1

        for w in status[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True
    # print(visited)  [False, True, False, True, True, False, True]
    if visited[S] == True and visited[G] == True:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # V: node, E = 간선 수
    status = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        status[v1].append(v2)
    S, G = map(int, input().split())
    print(f'#{tc}', dfs(S))
