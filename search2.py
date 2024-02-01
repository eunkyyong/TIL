# 학습자료 27/57
# lst에서 key를 찾아 인덱스를 return
# 못찾으면 -1을 return
def search(lst, N):
    for idx in range(N):
        # value = lst[idx]
        if lst[idx] == key:
            return idx
    return -1

def search(lst, N, key):
    idx = 0
    while idx<N and lst[idx] != key: # 단축평가
        idx += 1
    if idx<N: #index가 중간에 나옴
        return idx
    else:
        return -1

numbers = [4, 9, 11, 23, 2, 19, 7] #첫번째, 마지막 것 확인해야 함
N = len(numbers)
print(search(numbers, 4))
print(search(numbers, 7))
print(search(numbers, 9))
print(search(numbers, 100))
# ----------------------------------------------------------
def binSearch(lst, N, key): # 정렬된 데이터 써야 함. 36/57
    startp = 0  # startpoint
    endp = N-1
    while startp <= endp: # False일 때 = 못 찾았을 때 조건도 붙여야 함!
        middlep = (startp + endp) // 2 # 매번 middlepoint 정해짐.
        if lst[middlep] == key:
            return middlep
        if lst[middlep] > key: # 바로 위쪽이 return이라서 여기 if문 가능.
            endp = middlep - 1
        else:
            startp = middlep + 1
    return -1

# numbers = [4, 9, 11, 23, 2, 19, 7]
numbers = [2, 4, 7, 9, 11, 19, 23]
N= len(numbers)
print(search(numbers, N, 2))
print(search(numbers, N, 4))
print(search(numbers, N, 9))
print(search(numbers, N, 100))