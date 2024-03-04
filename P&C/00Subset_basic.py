def print_data(path):
    for idx in range(len(path)):
        if path[idx] == 1:
            print(arr[idx], end = ' ')
    print()  # 완전 탐색

def subSet(k):
    if k == N:  # 집합 내 원소들을 다 파악해야 함
        print(path)
        print_data(path)
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