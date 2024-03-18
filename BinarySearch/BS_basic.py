# Binary Search
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()

# 2. 이진 검색 - 반복문 버전
def binary_search(target):
    # 제일 왼쪽, 오른쪽 인덱스
    low = 0
    high = len(arr)-1
    # 탐색 횟수
    cnt = 0
    # 해당 숫자 찾으면 종료
    # 더 이상 쪼갤 수 없을 때까지 반복
    while low <= high:
        mid = (low+high)//2
        print(f'mid = {mid} / arr[mid] = {arr[mid]}')
        cnt += 1
        
        # 가운데 숫자가 정답이면 종료
        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
    # 못찾으면 -1 반환
    return -1, cnt

print(f'21 = {binary_search(21)}')
print(f'324 = {binary_search(324)}')
print(f'888 = {binary_search(888)} ')