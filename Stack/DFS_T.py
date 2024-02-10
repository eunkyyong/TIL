# def dfs(s):
#     st = []
#     visited = [False] * (N+1) # 0을 안쓰는 걸로 간주하고, 0을 빈것으로 남겨놓는 다고 생각
#
#     st.append(s)
#     while st:
#         v = st.pop()
#         if not visited[v]:
#             visited[v] = True
#             print(v)
#
#         for w in G[v]: # G하고 연결된 애들 찾아오기
#             if not visited[w]:  # 방문 안했으면 append 해줘.
#                 st.append(w)
#
#
# def dfs_recursion(v): # ??
#     print(v)
#     visited[v] = True
#
#     for w in G[v]:
#         if not visited[w]: # 갔던 곳 또가면 안됨 -> 방문표시 테이블: 함수 밖에다!!
#             dfs_r(w)
#
# def dfs_b(s): # 이게 제일 간단 버전
#     st = []
#     visited = [False] * (N+1) # 0을 안쓰는 걸로 간주하고, 0을 빈것으로 남겨놓는 다고 생각
#
#     st.append(s)
#     visited[s] = True  # 넣을 때 방문표시 하는 법!!
#
#     while st:
#         v = st.pop()
#             visited[v] = True
#             print(v)
#
#         for w in G[v]: # G하고 연결된 애들 찾아오기
#             if not visited[w]:  # 방문 안했으면 append 해줘.
#                 st.append(w)
#                 visited[w] = True
#
# N = 7 # 1~7
# E = len(l)
# # 비선형 구조 저장하는 방법을 알아보자.
# G = [[] for _ in range(N+1)]
# # print(G)
# # G[1].append(E)
# for i in range(0, E, 2):
#     v1 = l[i]
#     v2 = l[i+1]
#     G[v1].append(v2)
#     # 무방향 == 양방향
#     G[v2].append(v1)
# # print(G) [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
# # dfs(s)
# dfs(1)
# visited = [False]* (N+1)
# # dfs_r(1)
#########################################################
def dfs(s):
    st = []
    visited = [False] * (N+1) # 방문표시 넣는 곳 [False] -> 아직 방문 안함. 편의상 0부터 N까지 이므로 N+1
    st.append(s)
    visited[s] = True  # 방문 표시 넣는 리스트에 start point넣어둠. 여기서 부터 시작하니까 = 방문했으니까.

    while st:
        v = st.pop()
        print(v)  # 1번째인 start point. 경로 출력하는 것임!!

        for w in G[v]:  # w가 end point.
            if not visited[w]:
                st.append(w)
                visited[w] = True  # 이거는 방문표시list에 visited가 비지 않도록 확인해주는 건가??

s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
l = list(map(int, s.split()))
E = len(l)
N = 7  # 각 노드의 개수

#  G에 경로를 넣어줘야 함.
G = [[] for _ in range(N + 1)]
for i in range(0, E, 2):  # stri만 input하면 그래프 경로 알아서 찍어주는거??
    v1 = l[i]
    v2 = l[i + 1]
    G[v1].append(v2)
    G[v2].append(v1)
    # print(G)

dfs(5)  # s : 시작점!!!!!


# 단방향일 땐, G[v1].append(v2)만 해주면 됨
# G = [[] for _ in range(v + 1)]  # 나 변수 잘못 쓴 것 같은데.. 아님 이 코드의 위치가 잘못되었음. v가 item poped인데..
# for _ in range(E):  # 단방향?
#     v1, v2 = map(int, input().split())
#     G[v1].append(v2)

# # G 만들기 G - 각 노드가 연결된 상태 - 단방향이란 조건 없음 양방향.
# for i in range(0, E, 2):
#     v1 = l[i]
#     v2 = l[i + 1]
#     G[v1].append(v2)
#     G[v2].append(v1)
# print(G)


