# def toggle(c):
#     c = c%2 + 1
#
# def diag(x, y, c):
#     dx = [-1, 1, 1, -1]
#     dy = [1, 1, -1, -1]
#     toggle(c)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<N and 0<=ny<N and arr[nx][ny] == c:
#             toggle(c)
#
# def rc(x, y, c):
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     toggle(c)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<N and 0<=ny<N and arr[nx][ny] == c:
#             toggle(c)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[-1] * N for _ in range(N)]
    black = 0
    white = 0
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2-1] = 2

    for _ in range(M):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        arr[x][y] = c
        if c == 1:
            r_color = 2
        else:
            r_color = 1
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            nx = x + dx
            ny = y + dy
            # 나하고 다른 색인 동안 뒤로 가기!
            while 0<=nx<N and 0<=ny<N and arr[nx][ny] == r_color:
                nx += dx
                ny += dy
            # 같은 값을 찾아서 나온 경우
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == c:
                # 원래 좌표까지 색을 바꾼다.

                while not (nx == x and ny == y):
                    nx -= dx
                    ny -= dy
                    arr[nx][ny] = c

        # arr[x][y] = c
        # diag(x, y, c)
        # rc(x, y, c)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:  # else쓰지말고 끝까지 조심
                white += 1
    print(f'#{tc} {black} {white}')

