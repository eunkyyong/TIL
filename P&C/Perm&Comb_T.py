# def print_data(path):
#     for idx in path:
#         print(arr[idx], end = ' ')
#     print()  # 완전 탐색
#
# # N개의 데이터로 K개의 순열을 재귀로 만든다.
# def perm(k, N, K):
#     if k == K:
#         print(path)
#         print_data(path)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             path[k] = i
#             visited[i] = True
#             perm(k+1, N, K)
#             visited[i] = False
# arr = ['a', 'b', 'c', 'd', 'e']
# N = 5
# K = 3
# path = [-1] * K  # 5개 중에 3개 뽑는 것이므로
# visited = [False] * N
# # perm(0, N, K)
#
# def subSet(k):
#     if k == N:  # 집합 내 원소들을 다 파악해야 함
#         print(path)
#         print_data(path)
#         return
#
#     # for i in range(2):
#     #     path[k] = i
#     #     subSet(k+1)
#     path[k] = 0
#     subSet(k+1)
#
#     path[k] = 1
#     subSet(k+1)
#
#
# arr = ['a', 'b', 'c', 'd', 'e']
# N = 5
# K = 3
# path = [-1] * N  # 5개 중에 3개 뽑는 것이므로
# visited = [False] * N
# subSet[0]


# subSum의 합 구하기
def subSum_print(path):
    for idx in range(N):
        if path[idx]:
            print(arr[idx], end = ' ')
    print

def subSet(k):
    if k == N:  # 집합 내 원소들을 다 파악해야 함
        print(path)
        subSum_print(path)
        return

    # for i in range(2):
    #     path[k] = i
    #     subSet(k+1)
    path[k] = 0
    subSet(k+1)

    path[k] = 1
    subSet(k+1)


arr = ['a', 'b', 'c', 'd', 'e']
N = 5
K = 3
path = [-1] * N  # 5개 중에 3개 뽑는 것이므로
visited = [False] * N
subSet(0)