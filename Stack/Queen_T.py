# powerset
N = 10
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = [0, 0, 0, 0] => {}
# ..
# result = [0, 0, 1, 1] => {7, 12}
# result = [1, 1, 1, 1] => {11, 3, 7, 12}
# for i0 in [0,1]:
#     result[0] = i0
#     for i1 in [0, 1]:
#         result[1] = i1
#         for i2 in [0, 1]:
#             result[2] = i2
#             for i3 in [0, 1]:
#                 result[3] = i3
#                 print(result)
result = [-1] * N
def subset(k, subSum):
    if subSum>10:
        return

    if k==N:
        print(result, '=>', end = '')
        sumV = 0
        for i in range(N):
            if result[i]:  # 1인 경우에만!
                sumV += numbers[i]
        print(sumV)
        return


    for i in [0,1]:
        result[k] = i
        subset(k+1, )

subset(0, 0)
print(result)
#
