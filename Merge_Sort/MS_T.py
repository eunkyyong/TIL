# lst의 값들을 정렬한 후 return new_lst
def merge(left, right):
    new_lst = []
    # left_position
    lp = 0
    # right_position
    rp = 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else:
            new_lst.append(right[rp])
            rp += 1
        # 비교할 것이 없으면 끝내야 함
    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])

    return new_lst

def merge_sort(lst):
    print(lst)
    if len(lst) <= 1:
        return lst
    m = len(lst) // 2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    new_lst = merge(left, right)

    return new_lst

numbers = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_list = merge_sort(numbers)
print(sorted_list)