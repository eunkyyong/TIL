def dfs(y, x, path):
    # 기저조건: 7자리면 끝!
    if len(path) == 7:
        result.add(path)
        return

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny<0 or ny>=4 or nx<0 or nx>=4:
            continue
        dfs(ny, nx, path + maps[ny][nx])

T = int(input())
for tc in range(1, T+1):
    # 격자판 저장
    maps = [input().split() for _ in range(4)]
    # 중복 제거 위해 set 사용
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')