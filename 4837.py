arr = []
def f(arr, N): # 모든 부분집합 구하기
    # i가 0인 경우 공집합
    for i in range(1<<N): # 1<<N : 8==2**3 ==1000 (1<<3) binary.
        s = 0
        for j in range(N):
            if i & (1<<j):
                s += arr[j]
                # print(arr[j], end=" ")
        # print(s)
        if s == 0:
            return True
    return False
def subSet():
    # 위 부분집합 중 N개의 원소를 갖고, 원소의 합이 K인 부분집합의 개수


T = int(input())
for num in range(T):
    N, K = list(map(int, input().split()))
    a = f(arr, N)
    print(f'#{i + 1} {a}')