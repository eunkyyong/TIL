# def subSet(k):
#     if k==N:  # 재귀호출 시 빠져나갈 조건 필요함.
#         print(check)
#         for i in range(N):  # 원소 출력해줘.
#             if check[i]:
#                 print(numbers[i], end = ' ')
#         print()
#         return
#
#     for i in [0, 1]:
#         check[k] = i
#         subSet(k+1)
#
# N = 3
# numbers = [10, 30, 20]
# # check = [0, 0, 0] => {}
# # check = [0, 0, 1] => {20}
# # check = [1, 1, 1] => {10, 30, 20}
# #      k = 0, 1, 2
# check = [-1] * N
# subSet(0)
## 부분집합 합
def subSet(k):
    if k==N:  # 재귀호출 시 빠져나갈 조건 필요함.
        print(check)
        sumV = 0
        for i in range(N):  # 원소 출력해줘.
            if check[i]:
                sumV += numbers[i]
                # print(numbers[i], end = ' ')
        print(sumV)
        return

    for i in [0, 1]:
        check[k] = i
        subSet(k+1)

N = 3
numbers = [10, 30, 20]
# check = [0, 0, 0] => {}
# check = [0, 0, 1] => {20}
# check = [1, 1, 1] => {10, 30, 20}
#      k = 0, 1, 2
check = [-1] * N
subSet(0)

# Backtracking
def subSet(k, midS):

    if midS>30:     # Backtracking 이라 중간에 빠져나감을 눈에 잘 보이게 하기 위함.
        return

    if k==N:  # 재귀호출 시 빠져나갈 조건 필요함.
        print(check)
        print(midS)
        return

    for i in [0, 1]:
        check[k] = i
        if i == 0:
            subSet(k+1, midS)
        else:
            subSet(k + 1, midS+numbers[k])   # midS이 반복문에 영향을 주지 않도록.

N = 3
numbers = [10, 30, 20]
# check = [0, 0, 0] => {}
# check = [0, 0, 1] => {20}
# check = [1, 1, 1] => {10, 30, 20}
#      k = 0, 1, 2
check = [-1] * N
subSet(0, 0)