def pascal(N):
    for i in range(N):
        for j in range(i+1):
            if 1 <= j <= i-1:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            else:
                arr[i][j] = 1
    for row in range(N):
        for col in range(N):
            if arr[row][col] != 0:
                print(arr[row][col], end = ' ')
        print()
    return


T = int(input())
for tc in range(1, T+1):
     N = int(input())
     arr = [[0] * N for _ in range(N)]
     print(f'#{tc}')
     pascal(N)


