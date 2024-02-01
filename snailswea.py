def snail(newArr):
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    row = 0
    col = 0
    di = 1
    for _ in range(N*N):
        newArr[row][col] = di
        newR = row + dr[d] # 아직 안갔는데 예상 자리, 만약 못가면 방향 전환!
        newC = col + dc[d] # 원래자리 + dc[i]
        # print(newArr,newR,newC)
        if newR >= N or newC >= N or newR < 0 or newC < 0 or newArr[newR][newC]:
            # row, col의 d방향 좌표가 범위가 벗어났거나 새좌표에 값이 있으면
            d = (d+1)%4
        row = row + dr[d]
        col = col + dc[d]
        di += 1

# print(newArr)
    for row in range(N):
        for col in range(N):
            print(newArr[row][col], end =' ')
        print()
    return


T = int(input())
for i in range(T):
    N = int(input())
    newArr = [[0]*N for _ in range(N)]
    print(f'#{i+1}') # 한번에 두줄 하려면 이렇게 출력
    snail(newArr)

