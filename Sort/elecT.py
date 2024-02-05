def check():
    now = 0 # 현재 지점
    cnt = 0
    for i in range(1, M):
        if STOPS[i] - STOPS[i-1] > K:
            return 0
        if now+K < STOPS[i]:
            cnt += 1
            now = STOPS[i-1]
    return cnt

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    STOPS = [0] + list(map(int, input().split())) + [N]
    M += 2
    # now = 0
    # cnt = 0
    # for i in range(1, M):
    #     if STOPS[i] - STOPS[i-1] > K:
    #         result = 0
    print(f'#{tc} {check()}')
    # print(K, N, M, STOPS)