T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_v = 0
    for c in str1:
        cnt = 0
        for i in str2:
            if c == i:
               cnt += 1
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')
