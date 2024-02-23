F = int(input())
Max = 0
n_lst = []

for scnd in range(1, F+1):
    lst = []
    lst.append(F)
    lst.append(scnd)
    while True:
        if lst[-2]-lst[-1] < 0:
            break
        lst.append(lst[-2]-lst[-1])

    if Max < len(lst):
        Max = len(lst)
        n_lst = lst[:]

print(Max)
print(*n_lst)