def recu(row, col, midSum):
    global Min

    if row==N-1 and col == N-1:
        # print(path)
        # print(midSum)
        if Min > midSum:
            Min = midSum
        return

    if col+1<N:
        # path.append((row, col+1, arr[row][col+1]))
        # path.append(arr[row][col + 1])
        recu(row, col+1, midSum+arr[row][col+1])
        # path.pop()

    if row+1<N:
        # path.append((row+1, col, arr[row+1][col]))
        # path.append(arr[row + 1][col])
        recu(row+1, col, midSum+arr[row+1][col])
        # path.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 10*N
    path = [(0, 0, arr[0][0])]
    recu(0, 0, arr[0][0])
    print(f'#{tc} {Min}')