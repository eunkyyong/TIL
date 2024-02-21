Q = []
newNo = 1
while True:
    Q.append((newNo, 0))
    print(f'{newNo}가 줄을 선다.')
    newNo += 1
    no, candy = Q.pop(0)