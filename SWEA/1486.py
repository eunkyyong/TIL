def partial(k):
    if k==N:
        print(result)
        sumV = 0
        for i in range(N):
            if result[i]:
                sumV += numbers[i]
        print(sumV)
        return

    result[k] = 0
    partial(k+1)
    result[k] = 1
    partial(k+1)
    # 보통 안써서 그렇지, 있음!!
    return


numbers = [i for i in range(1, 6)]
N = len(numbers)
result = [-1] * N
partial(0)