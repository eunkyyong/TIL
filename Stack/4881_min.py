def perm(k, subSum):
    global min_v

    if subSum > min_v:
        return

    if k==N:
        # print(check)  # index 경우의 수
        total = 0
        for i in range(N):
            index = check[i]
            total += numbers[i][index]
            # print(numbers[i][index], end = ' ')
        # print(total)
        # print()
        if min_v > total:
            min_v = total
            # subSum = 0
        return

    for i in range(N):
        if not visited[i]:
            check[k] = i
            visited[i] = True
            perm(k+1, subSum+numbers[k][i])  # 각 행에서 하나의 원소, 열 인덱스 겹치면 안됨
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    check = [-1] * N
    visited = [False] * N
    min_v = 100
    perm(0, 0)
    print(f'#{tc} {min_v}')