# 부분집합 생성 방법
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
cnt = 0 # 반복문 들어오기 전에 해야 함.
for i in range(2**N):
    print(i, end='=>') # 각 집합의 원소들을 binary로 나타내는 것?
    sumV = 0
    # cnt = 0
    # (누적합 구하기 전에 초기화!)
    for j in range(3):
        t = i & (1<<j)
        if t & (1<<j):
            if sumV = 10:
                cnt += 1
            sumV += numbers[j]

            # print(numbers[j], end =' ')
            # j번째 bit가 1인 경우: 0001/0010/0100/01000
        # else:
        #     pass # 0인 경우
    print('=', sumV)

    # i의 0번째를 확인해서 1이면 '10'
    #     i&(1<<0) => 001 : 001/000 (0비트 숫자만 확인. ) => 1??
    # i의 1번째를 확인헤서'20'
    #     i&(1<<1) => 010 : 010/000 => 2
    # i의 2번째를 확인 '12'
    #     i&(1<<2) => 100 : 100/000 => 4

# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
# for i in range(1<<n): # 1<<n : 부분 집합의 개수
#     for j in range(n):  # 원소의 수만큼 비트를 비교함
#         if i & (1<<j):  # i의 j번 비트가 1인 경우
#             print(arr[j], end=",")    # j번 원소 출력
#     print()
# print()

# def f(arr, N):
#     # i가 0인 경우 공집합
#     for i in range(1<<N):
#         s = 0
#         for j in range(N):
#             if i & (1<<j):
#                 s += arr[j]
#                 # print(arr[j], end=" ")
#         # print(s)
#         if s == 0:
#             return True
#     return False

# N = int(input())
# arr = list(map(int, input().split()))
# print(f(arr, N))