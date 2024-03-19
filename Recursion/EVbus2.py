'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''
def solve(k, capacity, cnt):
    global minV
    if k==N:
        # print(result)
        if minV > cnt:
            minV = cnt
        return
    if capacity==0:
        return
    else:
        if minV < cnt:
            return

    result[k] = 0
    solve(k+1, capacity-1, cnt)
    result[k] = 1
    # print(k+1)
    solve(k+1, lst[k+1], cnt + 1)

T = int(input())
for tc in range(T):
    lst = list(map(int, input().split())) + [0]
    N = lst[0]
    result = [-1] * N
    minV = 100
    solve(1, lst[1], 0)
    print(f'#{tc+1} {minV}')
