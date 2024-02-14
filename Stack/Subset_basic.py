# def checknode(v):
#     if promising(v):
#         if there is a solution at v:
#             write the solution
#         else:
#             for u in each child of v:
#                 checknode(u)

# # Subset
def f(i, k): # k개의 원소를 가진 배열A, 부분집합의 합이 t인 경우
    if i==k:  # 모든 원소에 대해 결정하면
        ss= 0  # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:  # A[j]가 포함된 경우
                print(A[j], end = ' ')
                ss += A[j]
        print(ss)  # 부분집합 원소의 합
    else:
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bit = [0] * N
f(0, N)


# Subset 특정 합
def f(i, k, t): # k개의 원소를 가진 배열A, 부분집합의 합이 t인 경우
    if i == k:  # 모든 원소에 대해 결정하면
        ss = 0  # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:  # A[j]가 포함된 경우
                ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
    else:
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N
f(0, N, 10)

# i원소의 포함여부를 결정하면 i까지의 부분집합의 합 si를 결정할 수 있음
# Si-1이 찾고자 하는 부분집합의 합보다 크면 남은 원소를 고려할 필요가 없음
def f(i, k, s, t): # k개의 원소를 가진 배열A, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if s == t:  # 목표값이면
        for j in range(k):
            if bit[j]:
                print(A[j], end = ' ')
        print()
    elif i == k:  # 모든 원소를 고려했으나 s != t
        return
    elif s > t:  # 아직 남은 원소가 있긴 한데.. 커
        return
    else:
        # bit[i] = 1
        # f(i+1, k, s+A[i], t)
        # bit[i] = 0
        # f(i+1, k, s, t)
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, s+A[i]*j, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N
cnt = 0
f(0, N, 0, 55)
print(f'cnt:', cnt)



