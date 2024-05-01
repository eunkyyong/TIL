N = int(input())
lst = list(map(int, input().split()))
cnt = 0
# 반복문 돌면서
for i in lst:
    if i == 1:
        cnt += 1
        continue
    elif i == 2:
        continue
    # 2~i-1까지의 숫자로 나눴을 때 나누어 떨어지면 cnt
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break
# N - cnt
answer = N-cnt
print(answer)