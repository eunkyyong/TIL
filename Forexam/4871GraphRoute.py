import sys
sys.stdin = open("C:\cek\pycharm\TIL\Forexam\sample_input (7).txt", "r")

def dfs(S):
    st = []
    st.append(S)
    visited = [False] * (V+1)
    visited[S] = 1

    while st:
        v = st.pop()

        for w in status[v]:
            if not visited[w]:
                visited[w] = True
                st.append(w)

    if visited[S] == True and visited[G] == True:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    status = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        status[v1].append(v2)
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S)}')


