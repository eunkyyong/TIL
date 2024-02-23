for row in range(1, N):
    if newARRR[row].count('0') == M*4:
        continue
    col = M*4 -1
    while col >= 0:
        if newARR[row][col]=='1' and newARR[row-1][col] == '0':
            result = []
            for cnt in range(8):
                c = 0
                while newARR[row][col] == '1':
                    col -= 1
                    c += 1
                b = 0
                while newARR[row][col] == '0':
                    col -= 1
                    b += 1

                a = 0
                while newARR[row][col] == '0':
                    col -= 1
                    a += 1