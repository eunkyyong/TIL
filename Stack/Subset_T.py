N = 10
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [-1]* N
def construct_candidates(c):
    c[0] = 0
    c[1] = 1
    return 2

def subset(k, subSum):
    if subSum > 10:
        return

    if k==N:
        # if subSum == 10:
        #     print(result, subSum)
        process_solution(..)
        return

    c = [0] * 100
    ncandidates = construct_candidates()
    for i in range(ncandidates):
        result[k] = i
        subset(k+1)

    for i in [0, 1]:
        result[k] = i
        if i ==0:
            subset(k+1, subSum)
        else:
            subset(k+1, subSum+numbers[k])


subset(0, 0)
##
def subSet(k, midS):
    if k == N:
        print(check)
        print(midS)
        return

    if midS >= 30:
        return

    for i in [0,1]:
        check[k] = i
        if i == 0:
            subSet(k+1, midS)
        else:
            subSet(k+1, midS+numbers[k])