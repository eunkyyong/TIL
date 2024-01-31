T = int(input())
for tc in range(1, T+1):
    N = int(input())
    CMD = [list(map(int, input().split())) for _ in range(N)]
    # for i in CMD:
    # for r1, c1, r2, c2 color in CMD:
    #   print(r1, c1, r2, c2, color)
    brd = [[0]*10 for _ in range(N)] # 빈 곳 만들어주기
    # print(brd)
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1, c1, r2, c2, color)
        for r in range(r1, r2):
            for c in range(c1, c2):
                brd[r][c] += color
        print(brd)
        # brd[][] += color
    # for r in range(10):
    #     for c in range(10):
    #         if

    # cnt 어디서 초기화하고, 어디서 증가해야 할까.