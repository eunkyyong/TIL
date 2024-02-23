import sys
sys.stdin = open("C:\cek\pycharm\TIL\Forexam\input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r_max = 0  # 각 행의 합
    for r in range(100):
        r_sum = 0
        for c in range(100):
            r_sum += arr[r][c]
        if r_max < r_sum:
            r_max = r_sum

    # 각 열의 합
    c_max = 0
    for c in range(100):
        c_sum = 0
        for r in range(100):
            c_sum += arr[r][c]
        if c_max < c_sum:
            c_max = c_sum

    # 대각선의 합
    d_max = 0
    for r in range(100):
        d_sum = 0
        for c in range(100):
            if r == c:
                d_sum += arr[r][c]
            elif r+c == 100:
                d_sum += arr[r][c]
    if d_max < d_sum:
        d_max = d_sum

    lst = [c_max, r_max, d_max]
    print(f'#{N} {max(lst)}')