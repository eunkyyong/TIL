def perm(k):
    if k == N:
        print(result)
        for i in range(N):
            pos = result[i]
            print(numbers[pos], end = ' ')
        print()
        return
    for i in range(N):
        if not visited[i]:
            result[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False
            #i는 자료가 들어있는 인덱스임

    #
    # result[k] = 0
    # perm(k+1)
    # result[k] = 1
    # perm(k+1)
    # return
# numbers = [i for i in range(1, 4)]
numbers = [8, 1, 9, 7, 2, 5]
N = len(numbers)
result = [-1] * N
visited = [False] * N

perm(0)