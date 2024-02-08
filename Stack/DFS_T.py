
#
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
# # 넣을 때 visited 표시 하는 거 어때?
#########################################################
def dfs(s):
    st = []
    visited = [False] * (N+1) # 방문표시 넣을 것
    st.append(s)
    visited[s] = True

    while st: #합한 다음에 연결된 것 st에 넣자.
        v = st.pop()
        print(v)

        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True

# w가 end point.
# w가 여러 개일 때, visited 갖고 check
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
l = list(map(int, s.split()))

N = 7
E = len(l)

# G 만들기
# for i in range(0, E, 2):
#     v1 = l[i]
#     v2 = l[i+1]
#     G[v1].append(v2)
#     G[v2].append(v1)
# print(G)
dfs(5)  # s : 시작점!!!!!

G = [[] for _ in range(V+1)]
for _ in range(E):  # 단방향?
    v1, v2 = map(int, input().split())
    G[v1].append(v2)