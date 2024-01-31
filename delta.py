# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = 5
# arr = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0<=ni<N and 0<nj<N:
#                 print(arr[ni][nj])
N, M = map(int, input().split())
arr = [list(map(input().split())) for _ in range(N)]
print(N, M, arr)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(N, M, arr)

T = int(input())
for tc in range(1, T+1):

