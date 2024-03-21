def perm(k):
    global maxV
    if k == N:
        # print(result)
        prob = 1
        for i in range(N):
            pos = result[i]
            prob *= numbers[i][pos]
        prob /= 10000
        if maxV < prob:
            maxV = prob
        return
    else:
        multiply = 1
        for i in range(1, k+1):
            pos1 = result[i]
            multiply *= numbers[i][pos1]/100
        if multiply <= maxV/1000000:
            return


    for i in range(N):
        if visited[i] == False:
            result[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    result = [-1] * N
    maxV = 0
    perm(0)
    print(f'#{tc+1} {maxV:.6f}')
