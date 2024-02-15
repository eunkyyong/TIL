for i in range(10):
    tc = input()
    lst = list(map(int, input().split()))
    va = 1
    while True:
        item = lst.pop(0)
        item -= va

        if item > 0:
            lst.append(item)
            va = va % 5 + 1
        else:
            lst.append(0)
            break


    print(f'#{tc}', end = ' ')
    print(*lst)