def partition_h(s, e):
    p = len(numbers) // 2
    i = s
    j = e

    while i<=p:
        while i<=p and numbers[i] <= numbers[p]:
            i += 1
        while i<=p and numbers[j] > numbers[p]:
            j -= 1
        if i<j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[p], numbers[j] = numbers[j], numbers[p]
    return j

def quick_sort(s, e):
    if s<e:
        m = partition_h(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(0, numbers[-1])
    print(f'#{tc+1} {numbers[len(numbers)//2]}')
'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
