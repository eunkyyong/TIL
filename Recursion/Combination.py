# Combination with recursion
def dfs(level):
    if level == 3:
        print(*path)
        return

    for i in range(len(arr)):
        # 여기는 못가 ! (가지치기)
        # 백트래킹 코드 팁
        # 갈 수 없는 경우를 활용
        # 아래 코드처럼 갈 수 없을 때 continue
        if arr[i] in path:
            continue

        path[level] = arr[i]
        dfs(level+1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level] = 0


arr = [i for i in range(1, 4)]
path = [0] * 3

dfs(0)