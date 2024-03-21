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
    #   1. class 로 만들기 (강추)
    #   2. tuple로 관리 (두 개까지는 괜찮음...)
    #   - 이차원 배열 + 가중치, depth.. 등은 tuple 비추
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)
        print(now, '/', MST)
        # 우선순위 큐의 특성 상
        # 더 먼거리로 가는 방법이 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면, continue
        # 방문 했다면 continue
        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight
        
        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없다면 pass, 이미 방문했다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))
    print(f'최소비용: {sum_weight}')



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
prim(s)



