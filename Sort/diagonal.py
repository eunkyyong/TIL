arr = [list(map(int, input().split())) for _ in range(5)]
# 대각선 원소의 합 => (0,0) (1,1) ...(4,4).. (0,4) (1, 3) (2,2)
# 다 하고 (2,2) 한 개 빼주기.
total = 0
for i in range(5):
    if arr[i][i] != 0:
        total += arr[i][i]
    if arr[i][4-i] != 0:
        total += arr[i][4-i]
total = total - arr[5//2][5//2]
print(total)

# diagonal1-2
# 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
# 0~K까지 라면, 열이 K일때 K+1 이 있어야 하고, K=0일 때 K-1이있어야 계산 가능.
# i, j = 0 일 때,
arr = arr + [list(map(int, input.split())) for _ in range(N)]

for i in range(5):
    a