'''
3
3 35
11 10 19
4 826
559 281 278 27
5 572
88 255 570 839 39
'''
def dfs(cnt, sum_expense, k):
    global ans
    global ans_cnt
    # print(cnt, sum_expense, k)
    # 비용이 예산초과되면 종료한다
    if V < sum_expense:
        # 이전 함수로 돌아감
        return
    # 섬의 개수-1 보다 같거나 클 때, 예산보다 작을 때만 return
    # 예산 보다 작아도 최대 다리 개수가 N-1면 종료
    # print(cnt, sum_expense, k)
    if cnt == N:
        # 만약 다리 개수 같다면, 최소 비용 구해야 함
        # 최대 다리 개수 같을 때
        if k == ans_cnt:
            ans = min(ans, sum_expense)
        # 최대 다리 개수 다를 때, 그냥 그 이전으로?
        if k > ans_cnt:
            ans = min(ans, sum_expense)
            ans_cnt = max(k, ans_cnt)
        # print(ans_cnt, ans)
        return k, ans


    # 다리 하나 더 놓기
    # 오류나는 윗부분에 확인
    dfs(cnt +1, sum_expense+Ci[cnt], k+1)
    # 다리 하나 더 안두고 지나가기
    dfs(cnt+1, sum_expense, k)


T = int(input())
for tc in range(1, T+1):
    N, V = map(int, input().split())
    Ci = list(map(int, input().split()))
    ans = int(1e7)
    ans_cnt = int(0)
    dfs(0, 0, 0)
    print(ans_cnt, ans)