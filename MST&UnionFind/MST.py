import sys
sys.stdin = open("input.txt", "r")
# 우선순위 큐(pq = priority queue) 활용
from heapq import heappush, heappop

def prim(start):
    pq = []
    # 최소신장트리 visited 같은 느낌
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존] dfs node 번호만 관리
    # [prim] 우선순위가 weight에 따라 정리되어야 함.
    # [prim] 가중치가 낮으면 먼저 나와야 한다. (최소 신장 트리니까.)
    # [prim] -> 동시에 두 가지 데이터 다루기
    # 
    heappush(pq, )

V, E = map(int, input().split())
# 인접 행렬
# - [실습] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    # 출발, 도착, 가중치
    s, e, w = map(int, input().split())
    # 가중치 저장
    # [기존] 3 -> 4로 갈 수 있다.
    # graph[3][4] = 1

    # [가중치 graph] 3 -> 4로 가는데 31이라는 비용이 든다.
    # graph[3][4]= 31
    graph[s][e] = w
    # 무방향(쌍방향) 그래프
    graph[e][s] = w



