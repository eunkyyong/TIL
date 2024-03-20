# 인접 list -  bfs
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]
def bfs(start):
    v = [0]* 5
    queue = [start]
    v[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end = ' ')

        for to in graph[now]:
            if v[to]:
                continue
            v[to] = 1
            queue.append(to)

bfs(0)
