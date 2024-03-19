'''
3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4
'''

def perm(k):
    global minV
    if k == N:
        # print(result)
        sumV = 0
        for i in range(N):
            pos = result[i]
            sumV += numbers[i][pos]
            if sumV > minV:
                return
        if sumV < minV :
            minV = sumV
        # print(sumV)
        return
    else:
        sumV1 = 0
        for i in range(k):
            pos1 = result[i]
            sumV1 += numbers[i][pos1]
            if sumV1 > minV:
                return

    for i in range(N):
        if visited[i] == False:
            result[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    result = [-1] * N
    visited = [False] * N
    minV = 3000
    backT = 0
    perm(0)
    print(f'#{tc+1} {minV}')