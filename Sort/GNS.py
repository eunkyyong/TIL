import sys
sys.stdin = open("/Users/eunkyyong/PycharmProjects/pythonProject/TIL/Sort/GNS_test_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # print(f'{input()}')
    # input 들어온 것을 뒤에 str만 쪼개자.
    strr = list(map(str, input().split()))  # list로 나옴.
    N = len(strr)
    arr = [0]*10000
    # print(*strr) # SVN FOR ZRO NIN FOR EGT EGT TWO
    for i in strr:
        # ZRO = 0, ..., NIN = 9
        if i == 'ZRO':
            arr[0] += 1
        elif i == 'ONE':
            arr[1] += 1
        elif i == 'TWO':
            arr[2] += 1
        elif i == 'THR':
            arr[3] += 1
        elif i == 'FOR':
            arr[4] += 1
        elif i == 'FIV':
            arr[5] += 1
        elif i == 'SIX':
            arr[6] += 1
        elif i == 'SVN':
            arr[7] += 1
        elif i == 'EGT':
            arr[8] += 1
        elif i == 'NIN':
            arr[9] += 1
        for j in range(1, N+1):
            arr[j] += arr[j-1]
        temp = [0]*N
        for k in range(N-1, -1, -1):
            if strr[k] == 'ZRO':
                strr[k] = 0
            if strr[k] == 'ONE':
                strr[k] = 1
            if strr[k] == 'TWO':
                strr[k] = 2
            if strr[k] == 'THE':
                strr[k] = 3
            if strr[k] == 'FOR':
                strr[k] = 4
            if strr[k] == 'FIV':
                strr[k] = 5
            if strr[k] == 'SIX':
                strr[k] = 6
            if strr[k] == 'SVN':
                strr[k] = 7
            if strr[k] == 'EGT':
                strr[k] = 8
            if strr[k] == 'NIN':
                strr[k] = 9
                arr[strr[k]] -= 1  # 여기선 strr[k]가 str이라 불가능... zro = 0 할당 후 ?
                temp[arr[strr[k]]] = strr[k]
    print(f'#{tc}')
    print(temp)
