T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key = lambda x:x[1])
    idx = 0
    cnt = 0
    while idx<N:
        s = lst[idx][0]
        e = lst[idx][1]
        while idx<N and e > lst[idx][0]:
            idx += 1
        cnt += 1
    print(f'#{tc} {cnt}')