def step1():
    ST = []
    result = []
    icp = {'+':1, '*':2, '-':1, '/':2, '(':100}
    isp = {'+':1, '*':2, '-':1, '/':2, '(':0}
    for c in s:
        if c.isdigit():
            result.append(c)
        elif c ==

    while ST:
        result.append(ST.pop())
    return result

def step2(lst):
    ST = []
    for c in lst:
        if c.isdigit():
            ST.append(c)
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(calc(int(v1), int(v2), c))
    return ST.pop()

def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1-v2
    elif op == '*':
        return v1*v2
    else:
        return v1//v2

T = 10
for tc in range(1, T+1):
    number = input()
    s = input()
    post_order = step1()
    print(f'#{tc}', step2(post_order))