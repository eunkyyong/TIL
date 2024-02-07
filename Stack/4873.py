T = int(input())
for tc in range(1, T+1):
    s = input()
    stck = []
    stck.append(s[0])
    for i in range(1, len(s)):
        if len(stck) > 0:
            if s[i] != stck[-1]:
                stck.append(s[i])
            else:
                stck.pop()
        else:
            stck.append(s[i])
            continue

    if len(stck) == 0:
        result = False

    print(f'#{tc} {len(stck)}')