# quick_sort는 pivot을 젤 앞에 것 그리고 젤 뒤에 것으로 하는 알고리즘 공부.
# 보통 중간 pivot을 정하는 게 확률적으로 시간복잡도 낮음. 최악은 n**2
# s, e 사이에서 s 위치의 값을 pivot으로
# 좌측에는 작은 값들, 우측에는 큰 값들을 모으고
# return pivot's position
numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# numbers [x, x, 3, x, x, x, ...]
# 6, 4, 7, 8, 9, 3, 2, 1  ??
def partition_h(s, e):
    # (s, e) 범위에서 / pivot의 위치 s
    p = s
    i = s
    j = e
    while i<=j:
        # i 위치 이동, 왼쪽으로 모으기
        while i <= j and numbers[i] <= numbers[p]:
            i += 1
        # j 위치 이동
        while i <= j and numbers[j] > numbers[p]:
            j -= 1
        # pivot 제외하고 나머지 애들 바꾼 것. 이제 자기 자리 찾아가야 함.
        # 인접? 뒤집히면서 끝나서 마지막 데이터가 뒤집힌다. j가 마지막 데이터 갖고 있음.
        if i<j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    # 그래서 pivot 과 j 를 바꿔준다
    numbers[p], numbers[j] = numbers[j], numbers[p]
    # return pivot(position)
    return j
def quick_sort(s, e):
    # pivot 정하기
    if s<e:
        m = partition_h(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)

numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
N = len(numbers)
quick_sort(0, N-1)
print(numbers)