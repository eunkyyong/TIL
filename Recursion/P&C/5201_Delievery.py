
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wj = list(map(int, input().split()))
    tj = list(map(int, input().split()))
    wj.sort(reverse=True)
    tj.sort(reverse=True)

    idx = 0
    Sum = 0
    while idx < M:
        for i in range(len(wj)):
            if tj[idx] >= wj[i]:
                Sum += wj[i]
                wj.pop(i)
                break
        idx += 1  # 화물을 적재하든 지 적재 못하든 지 트럭의 idx는 증가시켜야 함.


    print(f'#{tc} {Sum}')
