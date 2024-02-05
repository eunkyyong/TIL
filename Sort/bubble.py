N = 6
arr = [7, 2, 5, 3, 1, 4]

# for j in range(N):
#     for i in range(N-1):
#         # bub_v = arr[i]
#         # bub_p = i
#         if arr[i] > arr[i+1]:
#             bub_v = arr[i]
#             bub_p = i
#             arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)
# --------------------------------
for i in range(N-1, 0, -1) # for i : N-1 -> 1, 감소하는 방향
# for j : 0 -> i-1 , j 비교할 두 원소 중 왼쪽의 인덱스
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)