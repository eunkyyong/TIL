T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = [0] + list(map(int, input().split()))
    # 화덕fireplace 크기만큼 피자(치즈 양) 넣기
    # 한 바퀴씩 돌릴 때마다 치즈 줄어들고 치즈 0 되면 빼기
    fp = [0] * N
    nextPizzaNo = 1
    while fp:
        pizzaNo = fp.pop(0)
        Ci[pizzaNo] //= 2
        if Ci[pizzaNo] == 0:
        # 남은 피자가 있을 때 화덕에 남은 피자 넣기
        # Next pizza 하고 m하고의 관계
            if nextPizzaNo <= M:
                fp.append(nextPizzaNo)
                nextPizzaNo += 1
        else:
            fp.append(pizzaNo)

    print(f'#{tc} {pizzaNo}')



