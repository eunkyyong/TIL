def step2(lst):
    ST = []
    try:
        # .이 중간중간에 나오는 경우
        for c in lst:
            if c.isdigit():
                ST.append(c)
            elif c == '.':

            else:
                if len(ST) >= 2:
                    v2 = ST.pop()
                    v1 = ST.pop()
                    ST.append(calc(int(v1), int(v2), c))
                else:
                    return 'error'
        if len(ST) >= 2:
            return 'error'
        return ST.pop()
    except:
        return 'error'




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
    # print(s)
    print(f'#{tc}', step2(s))
