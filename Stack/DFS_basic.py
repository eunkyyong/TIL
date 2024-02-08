# 나의 형제 노드보다 자식 노드를 먼저 보자.
# 내게 연결 된 것을 자식 노드라고 생각한다면..
def dfs(i, V): # 시작 i, 마지막 V
    visited = [0]*(V+1)  # visited, stack 생성 및 초기화
    st = []
    visited[i] = 1  # 시작점 방문
    print(i)  # 정점에서 할 일
    while True:  # 탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점w가 있으면
        for w in adjl[i]:
            if visited[w] == 0:
                st.append(i)  # push(i), i를 지나서
                i = w         # w에 방문
                visited[i] = 1  # 방문해서 할 일
                print(i)
                break   # for w
        else:  # for w, i에 남은 인접 정점이 없으면
            if st:  # 스택이 비어있지 않으면(지나온 정점이 남아있으면)
                i = st.pop()
            else:  # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break  # while True
    return

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접 리스트
adjl = [[] for _ in range(V+1)] # adjl에 인접인 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)  # 비어있는 행에 가서 n2를 추가해줘
    adjl[n2].append(n1)  # 방향이 없는 경우, 이 행이 추가되어야 한다! 이 행 없으면 엉뚱한 탐색함.
dfs(1, V)