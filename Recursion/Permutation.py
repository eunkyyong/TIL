# 구조 먼저 잡고 나서, 필요한 변수들을 parameter로 잡자!
def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때까지 반복
    if level == 3:
        print(*path)
        return

        # 들어가기 전
        # 다음 재귀 호출
        # - 다음에 갈 수 있는 곳들은 어디인가?
        # - 이 문제에서는 세 가지(len(arr)만큼) 경우의 수가 존재!
        # for i in range(len(arr)):
        # 현재 레벨 기록 후 다음 레벨 호출
    path[level] = 1
    dfs(level + 1)

    path[level] = 2
    dfs(level + 1)

    path[level] = 3
    dfs(level + 1)


arr = [i for i in range(1, 4)]
path = [0] * 3
# 갔다와서 할 로직

dfs(0)