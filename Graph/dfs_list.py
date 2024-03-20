graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]
visited = [0] * 5
path = []

def dfs(now):
    # 다음 재귀 호출 - 인접 리스트
    # 차이점1: 갈 수 없는 조건 필요 없음
    # 차이점2: for문 작성 수정
    # dfs: 현재 노드에서 다른 노드들을 확인 (후보군)
    # 다른 노드들 == 반복문
    for to in graph[now]:
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)
    # 돌아왔을 때 작업


dfs(0)