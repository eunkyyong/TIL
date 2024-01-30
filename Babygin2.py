N = 3
numbers = [0, 1, 2]
for i in range(3):
    for j in range(3):
        if i==j:
            continue #(반복안하고 다시 위로 올라갈 때)
        for k in range(3):
            if k==i or k==j:
                continue
            print(i, j, k) # i, j, k는 위치를 나타내는 인덱스.
            # numbers[i], numbers[j], numbers[k]가 되어야 함