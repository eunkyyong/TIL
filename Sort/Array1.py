# 젤 왼쪽 상자 기준, 방의 가로 길이 100 - 1 - 높이에 따라 그 행에 몇개 있는 지
def gravity(N):
    for i in range(arr[0]):
        # 100 -i번째 행에 있는 상자 -1
        # 0번째 - 높이 1이상인 것, 1번째  - 높이 2이상인 것...
        cnt = 0
        differ = 0
        for num in range(N):
            if arr[num] > i:
                cnt += 1
        differ = 100 - cnt - 1

        max_v = 0
        if differ > max_v:
            max_v = differ
    return max_v

N = int(input())
arr = list(map(int, input().split()))
# print(*arr)
print(gravity(N))