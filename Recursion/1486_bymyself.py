'''
1
5 16
1 3 3 5 6
'''
def dfs(cnt, sum_height):  # 재귀 도니까 변수 명 통일해줘야 함!! 그 전의 값이 안바뀜!!!
    global ans
    if sum_height >= B:
        ans = min(ans, sum_height)
        return
    if cnt == N:
        return

    dfs(cnt+1, sum_height+arr[cnt])
    dfs(cnt+1, sum_height)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e6)
    dfs(0, 0)
    print(f'#{tc} {abs(ans-B)}')