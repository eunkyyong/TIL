def step2(lst):
    ST = []
    lst.pop()
    for c in lst:
        if c.isdigit():
            ST.append(c)
        else:
            try:
                v2 = ST.pop()
                v1 = ST.pop()
                ST.append(calc(int(v1), int(v2), c))
            except:
                return 'error'
    if or len(ST) != 1:
        return 'error'
    return ST.pop()


def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '*':
        return v1 * v2
    elif op == '-':
        return v1 - v2
    else:
        return v1/v2


T = int(input())
for tc in range(1, T+1):
    s = list(input().split())
    error = False
    # print(s)
    print(f'#{tc}', step2(s))