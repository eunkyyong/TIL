T = int(input())
for tc in range(T):
    N = int(input())
    CMD = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # print(CMD) # [[2, 2, 4, 4, 1], [3, 3, 6, 6, 2]]
    brd = [[0] * 10 for _ in range(10)]  # 빈 곳 만들기
    for r1, c1, r2, c2, color in CMD:
        # print(r1, c1, r2, c2, color) # <class 'int'>
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                brd[r][c] += color
            # print(brd) # 잘 들어감!
    for r in range(10):
        for c in range(10):
            if brd[r][c] > 2:
                cnt += 1
    print(f'#{tc+1} {cnt}')
