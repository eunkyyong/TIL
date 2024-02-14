def perm(k):
    if k==N:
        print(check)
        for i in range(N):
            index = check[i]
            print(numbers[index], end = ' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            check[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False  # return 만나면 해제, container type이라서 다음 반복문에 영향을 주기 때문에 다시 원상복구 시킴.
            # 교환 방식은 앞에 했던 건 이미 방문했다고 간주.


# 순열은 인덱스 기준으로 생각하기
N = 3
numbers = [10, 30, 20]
check = [-1] * N
visited = [False] * N
# check = [0, 1, 2] => [10, 30, 20]
# check = [2, 0, 1] => [20, 10, 30]
perm(0)