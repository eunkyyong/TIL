T = int(input())
for tc in range(1, T+1):
    ST = []
    s = input()
    pair = {'}':'{', ')':'('}
    result = 1
    for c in s:
        if c in ['(', '{']:
            ST.append(c)
        elif c in [')', '}']:
            if len(ST) == 0 or ST.pop() != pair[c]:
                result = 0
                break
    if result ==1 and len(ST)>0:
        result=0
    print(f'#{tc} {result}')
