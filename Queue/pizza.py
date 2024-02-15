T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = [0] + list(map(int, input().split()))
    # 화덕fireplace 크기만큼 피자(치즈 양) 넣기
    # 한 바퀴씩 돌릴 때마다 치즈 줄어들고 치즈 0 되면 빼기
    fp = [0] * N
    nextPizzaNo = 1
    while fp:
        # pizzaNo = numb.pop[0]
        # pizzaNo == 1일 때, 치즈양?
        # 치즈가 0이면 피자 다시 넣지 않고 새 피자 넣기
        if cheese == 0:
            if Ci:  # 남은 피자가 있을 때 화덕에 남은 피자 넣기
                piz = Ci.pop(0)
                fp.append(piz)
                numb[i] = piz
            else:  # 남은 피자 없을 때
                numb[i] =
                continue
        # fp에 남은 피자가 하나고 치즈 양이 0일 때 break
        if len(fp) ==1 and cheese == 0:
            break

    print(f'#{tc}', end = ' ')
    print(fp[0])



