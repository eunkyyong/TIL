N = 10
result = [-1] * N
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def subSum(k, curS):
    if curS > 10:
        return

    if k == N:
        if curS == 10:
            print(result)
            for i in range(N):
                if result[i]:
                    print(numbers[i], end = ' ')
            print()  # 원소로 찍어보기
        return


    for d in [0,1]:
        result[k] = d
        if d==0:
            subSum(k+1, curS)
        else:
            subSum(k+1, curS + numbers[k])

subSum(0, 0)
#        for i in range(N):
#             if result[i]:
#                 sumV += numbers[i]
#         if sumV == 10:
#             print(result)
#             for i in range(N):
#                 if result[i]:
#                     print(numbers[i], end = ' ')
#             print()
#         return