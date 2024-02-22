def decTobin(intV):
    s = ''
    # while intV > 0:
    # 자릿수 정해져 있을 때
    for _ in range(4):
        s = str(intV%2) +s
        intV //= 2
    return s

print(decTobin(2))