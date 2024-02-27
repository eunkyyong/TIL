def perm(k, midSum):
    global Min

    if k==N:
        print(path)
        print(midSum)
        if Min > midSum:
            Min = midSum
        return

    for i in range(N):
        if not used[i]:
            path[k] = i
            used[i] = True
            s = path[k-1]
            e = path[k]
            perm(k+1, midSum + abs(x[path[k]]-x[]) + abs(y[path[k]]-y[]))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = []
    y = []
    lst = list(map(int, input().split()))
    for i in range(0, N*2+1, 2):
        x.append(lst[i])  # [0, 100, 70, 30, 10, 90]
        y.append(lst[i+1])  # [0, 100, 40, 10, 5, 70]
    path = [-1] * N
    used = [False] * N
    print(x)
    print(y)
    used[0] = True
    path[0] = 0
    Min = 100*N
    perm(1, 0)
    print(f'#{tc} {Min}')