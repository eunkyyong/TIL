arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def f(arr): # 모든 부분집합 구하기
    # i가 0인 경우 공집합
    ans = 0
    for i in range(1<<12): # 1<<N : 8==2**3 ==1000 (1<<3) binary.
        s = 0 # 부분집합 원소의 합
        cnt = 0 # 부분집합의 개수
        for j in range(12):
            t = i & (1<<j) # i는 (0 ~ 1<<N)
            if t:
                s += arr[j]
                cnt += 1

        if s == K and cnt == N:
            ans += 1
    return ans

# def subSet():
    # 위 부분집합 중 N개의 원소를 갖고, 원소의 합이 K인 부분집합의 개수
T = int(input())
for num in range(T):
    N, K = list(map(int, input().split()))
    a = f(arr)
    print(f'#{num + 1} {a}')