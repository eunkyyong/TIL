# Binary Search
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()
# 2. recursion 버전
def binary_search(target, high, low):
    # 기저조건 (언제까지 재귀가 반복되어야 할까?)
    if low > high:
        return -1
    # 다음 재귀 들어가기 전엔 무엇을 해야 할까?
    # -> 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀 함수 호출 (파라미터)
    if target < arr[mid]:
        return binary_search(target, mid-1, low)
    else:
        return binary_search(target, high, mid+1)

    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야 할까?
print(f'21 = {binary_search(21, len(arr)-1, 0)}')
print(f'324 = {binary_search(324, len(arr)-1, 0)}')
print(f'888 = {binary_search(888, len(arr)-1, 0)} ')