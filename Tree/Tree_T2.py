N = int(input())
lst = list(map(int, input().split()))
# TREE = [[] for _ in range(N+1)]
leftC = [0] * (N+1)
rightC = [0] * (N+1)

for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]
    if leftC[p] == 0:
        leftC[p] = c
    else:
        rightC[p] = c
print(leftC)
print(rightC)
