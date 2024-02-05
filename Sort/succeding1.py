T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = input()
    maxV = 0
    cnt = 0
    for c in S:
        if c == '1': # 문자열
            cnt += 1
        else:
            if maxV < cnt:
                maxV = cnt
            cnt = 0
    # print(cnt) # 끝이 1로 끝나면 예외니까 한번 더 계산해줘라.
    if maxV < cnt:
        maxV = cnt
    print(f'#{tc} {maxV}')

