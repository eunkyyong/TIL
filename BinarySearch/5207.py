def binary_search(target):
    low = 0
    high = N-1
    d = 0 # 무방향, 1: 왼쪽, 2: 오른쪽

    while low <= high:
        mid = (low+high)//2

        if A[mid] == target:
            return 1
        elif A[mid] > target:
            if d==1:
                return 0
            d = 1
            high = mid - 1
        elif A[mid] < target:
            if d == 2:
                return 0
            d = 2
            low = mid + 1
    return 0

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    num = 0
    for i in range(M):
        target = B[i]
        num += binary_search(target)

    print(f'#{tc+1} {num}')
'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''