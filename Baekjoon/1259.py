N = -1
while N!='0':
    N = input()
    if N != '0' and N[::-1] == N:
        print('yes')
    elif N[::-1] != N:
        print('no')
    elif N == '0':
        break