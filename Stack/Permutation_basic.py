# 필요한 데까지만 백트래킹해서 순열 만들기!!
# 1. 모든 순열 만들기
# def f(i, k):
#     if i == k:
#         print(*P)
#     else:
#         for j in range(i, k):  # P[i](i행에서 선택한 열)자리에 올 원소 P[j] 결정해준다.
#             P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
#             f(i+1, k)
#             P[i], P[j] = P[j], P[i]  # 교환 전으로 복구!
#
#
# N = 3
# P = [1, 2, 3]
# f(0, N)
# 실습
def f(i, k):
    global cnt
    global min_v
    cnt += 1
    if i == k:
        # print(*P)
        s = 0   # 선택한 원소의 합
        for j in range(k):
            s += arr[j][P[j]]   # j행에서 P[j] 열을 고른 경우의 합 구하기
        if min_v > s:
            min_v = s

    else:
        for j in range(i, k):  # P[i](i행에서 선택한 열)자리에 올 원소 P[j] 결정해준다.
            P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]  # 교환 전으로 복구!


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100  # 문제에 따라 다름
cnt = 0
f(0, N)
print(min_v, cnt)

# 실습
def f(i, k, s):   # i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i == k:
        # print(*P)
        s = 0
        for j in range(k):
            s += arr[j][P[j]]
        if min_v > s:
            min_v = s

    else:
        for j in range(i, k):  # P[i](i행에서 선택한 열)자리에 올 원소 P[j] 결정해준다.
            P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]  # 교환 전으로 복구!


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100  # 문제에 따라 다름
cnt = 0
f(0, N, startpoint)
print(min_v, cnt)
