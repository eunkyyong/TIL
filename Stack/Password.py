import sys
sys.stdin = open("C:\cek\pycharm\TIL\Stack\input (6).txt", "r")
for tc in range(1, 11):
    N, s = input().split()
    N = int(N) # s는 받아오면 str, 고칠 필요가 없음!!!
    stck = []
    stck.append(s[0])
    for i in range(1, N):
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

    st = ''.join(stck)
    st = int(st)
    print(f'#{tc} {st}')
