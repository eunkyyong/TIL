def perm(k, s):
    sumV = 0
    if k == K:
        print(result)
        for i in range(K):
            pos = result[i]
            sumV += numbers[pos]
        print(sumV)
        return
    for i in range(s, N-K+1+k):
        result[k] = i
        perm(k+1, i+1)
        print(k+1)
        #i는 자료가 들어있는 인덱스임
        # result 는 인덱스가 들어있는 리스트.
    return


# numbers = [i for i in range(1, 4)]
numbers = [8, 1, 9, 7, 2, 5]
N = len(numbers)
K = 3
result = [-1] * K
visited = [False] * N

perm(0, 0)