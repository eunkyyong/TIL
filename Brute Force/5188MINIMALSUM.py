'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''
def recu(row, col, midSum):
    global Min

    if row == N-1 and col == N-1:
        if Min > midSum:
            Min = midSum
        return

    if col+1<N:
        recu(row, col+1, midSum+arr[row][col+1])

    if row+1<N:
        recu(row+1, col, midSum+arr[row+1][col])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 10*N
    path = [(0, 0, arr[0][0])]
    recu(0, 0, arr[0][0])
    print(f'#{tc} {Min}')