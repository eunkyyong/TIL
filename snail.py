# 56/57
'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''
def getMin(arr, value):
    minV = 1e10
    for r in range(N):
        for c in range(N):
            if arr[r][c] < minV and arr[r][c] > value:
                minV = arr[r][c]
    return minV

def snail(arr):
    value = 0
    row = 0
    col = 0
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    for _ in range(N*N):
        value = getMin(arr, value) # 최솟값을 넣어서 또 getMin 함수 돌림! 리뷰!!
        newArr[row][col] = value # newA 0,0에 최솟값 넣음

        newR = row + dr[d] # 아직 안갔는데 예상 자리, 만약 못가면 방향 전환!
        newC = col + dc[d] # 원래자리 + dc[i]
        if newR >= N or newC >= N or newR < 0 or newC < 0 or newArr[newR][newC]: # row, col의 d방향 좌표가 범위가 벗어났거나 새좌표에 값이 있으면
            d = (d+1)%4
        row = row + dr[d]
        col = col + dc[d]


# print(newArr)
    for row in range(N):
        for col in range(N):
            print(newArr[row][col], end =' ')
        print()
    return

N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
newArr = [[0]*N for _ in range(N)]
snail(arr)
# print(snail(arr))
# print(getMin(20)) # 21
# print(getMin(10)) # 11