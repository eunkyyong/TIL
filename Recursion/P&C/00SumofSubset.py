# subSet의 합 구하기
def subSum_print(path):
    Sum = 0
    for idx in range(N):
        if path[idx]:
            Sum += arr[idx]
    print(Sum)
    print()

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


arr = [1, 2, 3, 4, 5]
N = 5
K = 3
path = [-1] * N  # 5개 중에 3개 뽑는 것이므로
visited = [False] * N
subSet(0)
