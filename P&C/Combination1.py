arr = ['A', 'B', 'C', 'D', 'E']
path = []

def KFC(x, start):
    if x == 3:
        print(path)
        return

    for i in range(start, 5):
        path.append(i)
        KFC(x+1, i+1)
        path.pop()
KFC(0, 0)