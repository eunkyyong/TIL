# pattern1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
# pattern2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
def black(arr, pattern1, pattern2):
    b_cnt = 0
    for j in range(8):
        if j % 2 == 0:
            for i in range(8):
                if arr[r+j][c+i] != pattern2[i]:
                    b_cnt += 1
        elif j % 2 == 1:
            for i in range(8):
                if arr[r+j][c+i] != pattern1[i]:
                    b_cnt += 1
    return b_cnt

# wbwb white_check 일 때
def white(arr, pattern1, pattern2):
    w_cnt = 0
    for j in range(8):
        if j % 2 == 0:
            for i in range(8):
                if arr[r+j][c+i] != pattern1[i]:
                    w_cnt += 1
        elif j % 2 == 1:
            for i in range(8):
                if arr[r+j][c+i] != pattern2[i]:
                    w_cnt += 1
    return w_cnt

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
pattern1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
pattern2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
Min = 2500
for r in range(N - 7):
    for c in range(M - 7):
        b_cnt = black(arr, pattern1, pattern2)
        w_cnt = white(arr, pattern1, pattern2)
        # print(f'r:{r}, c:{c}', b_cnt, w_cnt)
        min_cnt = min(b_cnt, w_cnt)
        if Min > min_cnt:
            Min = min_cnt
print(Min)