# a에서 b로 가는데 최단 경로는 무엇인가
# 모든 점까지 가는데 걸린 최소 거리 값을 구할 수 있다.
# 방향 그래프
import sys
sys.stdin = open('input1.txt', 'r')
INF = int(1e6)
def dijk(now):
    U = []
    D = [INF] * V
    D[now] = 0

    while len(U) < V:
        minV = INF
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        for i in range(V):
            if i in U: continue
            if G[now][i]:
                # 지금까지 들어있는 값+엣지값과의 최솟값/ 한 점까지 온 거리 모두와 이 경로와 비교해서 최솟값 구하기
                D[i] = min(D[i], D[now]+G[now][i])
                print(U, D)

V, E = map(int, input().split())
G = [[0]* V for _ in range(V)]

for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w
print(G)
dijk(0)

#
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

# INF = int(1e6)
# def dijk(now):
#     U = []
#     D = [INF] * V
#
#     D[now] = 0
#     while len(U) < V:
#         minV = INF
#         for i in range(V):
#             if i in U: continue
#             if D[i] < minV:
#                 minV = D[i]
#                 now = i
#
#         U.append(now)
#
#         for i in range(V):
#             if i in U: continue
#             if G[now][i]:
#                 D[i] = min(D[i], D[now]+G[now][i])
#
#     print(U, D)
#
# V, E = map(int, input().split())
# G = [[0]*V for _ in range(V)]
#
# for i in range(E):
#     v1, v2, w = map(int, input().split())
#     G[v1][v2] = w
#
# # print(G)
# dijk(0)
