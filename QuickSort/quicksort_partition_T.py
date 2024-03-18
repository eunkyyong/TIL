def partition_l(s, e):
    # pivot을 end로
    p= e 
    i = s-1
    for j in range(s, e):
        # j는 처음부터 쭉 도는 용도
        # i를 비교
        if numbers[j] < numbers[p]:
            i += 1
            # 자기 자신을 비교하는 것으로 간주. i=j
            numbers[i], numbers[j] = numbers[j], numbers[i]
        # numbers[j] > numbers[p]일 땐 i 아무것도 안 더해줌, i!=j되기 시작.
    # 다 끝나고 pivot의 위치를 찾아가야 함.
    numbers[i+1], numbers[p] = numbers[p], numbers[i+1]
    return i+1

def quick_sort(s, e):
    # pivot 정하기
    if s<e:
        m = partition_l(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)

numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
N = len(numbers)
quick_sort(0, N-1)
print(numbers)