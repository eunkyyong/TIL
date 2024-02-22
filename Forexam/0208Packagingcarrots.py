'''
3
3
1 2 3
5
1 1 1 2 3
8
1 2 3 4 5 6 7 8
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))

    # 소, 중, 대 박스 - count 들어갈 배열 (당근 크기는 idx)
    narr = [0] * 31
    for i in range(max(Ci)+1):
        narr[i] = Ci.count(i)

    Min = N
    for l1 in range(1, max(Ci)-1):
        for l2 in range(l1+1, max(Ci)):
            carB = [0]*3
            dif = 0
            # carB[i] != 0 How?
            for l in range(0, l1+1):
                carB[0] += narr[l]
            for l in range(l1+1, l2+1):
                carB[1] += narr[l]
            for l in range(l2+1, max(Ci)+1):
                carB[2] += narr[l]
            if carB[0]==0 or carB[1]==0 or carB[2]==0:
                continue
            if carB[0] > N//2 or carB[1] > N//2 or carB[2] > N//2:
                continue

            dif = max(carB)-min(carB)
            if Min > dif:
                Min = dif

    # 한번도 Min에 안들어갔으면 -1
    if Min == N:
        Min = -1

    print(f'#{tc} {Min}')