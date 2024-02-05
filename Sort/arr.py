# arr = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# print(arr[0]) # [1, 1, 1]

N = 3
M = 4
arr = [[1, 1, 1, 10],
       [2, 2, 2, 20],
       [3, 3, 3, 30]]
maxV = 0
for row in range(N):
    sumV = 0
    for col in range(M):
        # print(arr[row][col]) 전체 데이터 한번 씩 봄
        sumV += arr[row][col]
        # print(sumV)
    if maxV < sumV:
        maxV = sumV
print(maxV)

sumV = 0 # 전체 합
for row in range(N):
    for col in range(M):
        sumV += arr[row[col]]

for col in range(M):
    sumV = 0
    for row in range(N):
        sumV += arr[row][col] # col=0으로 놓고 row(M)부터 합 계산.
    print(sumV)