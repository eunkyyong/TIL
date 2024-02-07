for tc in range(1, 11):
    N, s = map(int, input().split())
    lst = []
    # lst 만들
    for _ in range(10):
        rem = s%10
        lst.append(rem)
        s = s//10
    # print(lst) [4, 8, 0, 9, 9, 0, 8, 3, 2, 1]
    stck = []
    stck.append(lst[0])
    # print(stck)
    for i in range(1, len(lst)):
        if len(stck) > 0:
            if lst[i] != stck[-1]:
                stck.append(lst[i])
            else:
                stck.pop()
        else:
            stck.append(lst[i])
            continue

    if len(stck) == 0:
            result = False
    num = 0
    for j in range(len(stck)):
        num += stck[j]*10**j
    print(f'#{tc} {num}')
