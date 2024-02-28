def combi(k, start):
    if k==K:
        print(path)
        return
    for i in range(start, N):
        path[k] = i
        combi(k+1, i+1)
    return

N = 5
K = 3
path = [-1] * K
combi(0, 0)