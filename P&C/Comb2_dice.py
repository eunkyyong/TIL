path = []

def dice(x, start):
    if x == 3:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        dice(x+1, i)  # i+1 이 아니라, 주사위 독립시행이므로 i.
        path.pop()
dice(0, 1)
