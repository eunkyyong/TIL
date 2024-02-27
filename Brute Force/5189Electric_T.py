'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''
# 중간합 구해서 빠져나가면 더 좋음
def perm(k, midSum):  # k = depth
    global Min
    if k==N:  # append방식말고 k번째 값에 집어넣기
        midSum += arr[path[N-1]][0]
        # print(midSum)
        # print(path)
        if Min > midSum:
            Min = midSum
        return

    for i in range(N):
        if not used[i]:
            path[k] = i
            used[i] = True  # 사용하는 것은 i.
            s = path[k-1]
            e = path[k]
            perm(k+1, midSum + arr[path[k-1]][i])
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = [-1] * N
    used = [False] * N

    used[0] = True
    path[0] = 0  # 옆 1, 2는 버린 것임
    Min = 1000
    perm(1, 0)
    print(f'#{tc} {Min}')