# N개의 데이터로 K개의 순열을 재귀로 만든다.
def print_data(path):
    for idx in path:
        print(arr[idx], end = ' ')
    print()  # 완전 탐색

def perm(k, N, K):
    if k == K:
        print(path)
        print_data(path)
        return

    for i in range(N):
        if not visited[i]:
            path[k] = i
            visited[i] = True
            perm(k+1, N, K)
            visited[i] = False
arr = ['a', 'b', 'c', 'd', 'e']
N = 5
K = 3
path = [-1] * K  # 5개 중에 3개 뽑는 순열
visited = [False] * N
perm(0, N, K)