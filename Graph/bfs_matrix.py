# 인접 행렬 bfs
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]
# 갈 수 있는 곳 다 가기
# 방문 순서대로 다음 노드
# 먼저 방문 -> 먼저 다음 노드 FIFO

def bfs(start):
    v = [0]* 5
    queue = [start]
    v[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end = ' ')

        for to in range(5):
            if graph[now][to] == 0:
                continue
            if v[to]:
                continue
            v[to] = 1
            print(v)
            queue.append(to)

answer = bfs(0)
