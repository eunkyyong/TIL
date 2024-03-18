'''
[69, 10, 30, 2, 16, 8, 31, 22]
[69, 10, 30, 2]
[69, 10]
[69]
[10]
[30, 2]
[30]
[2]
[16, 8, 31, 22]
[16, 8]
[16]
[8]
[31, 22]
[31]
[22]
[2, 8, 10, 16, 22, 30, 31, 69]
'''
def merge(left, right):
    new_lst = []
    lp = 0
    rp = 0
    while lp < len(left) and rp < len(right):
        if left[lp] <= right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else:
            new_lst.append(right[rp])
            rp += 1
    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])
    return new_lst

def merge_sort(lst):
    global num
    if len(lst) <= 1:
        return lst
    m = len(lst) // 2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    if left[-1] > right[-1]:
        num += 1

    new_lst = merge(left, right)

    return new_lst

T = int(input())
for tc in range(T):
    N = int(input())
    num = 0
    numbers = list(map(int, input().split()))
    sorted_list = merge_sort(numbers)
    half = len(sorted_list) //2
    print(f'#{tc+1} {num} {sorted_list[half]}')
'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''