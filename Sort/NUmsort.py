# def asc(numbers):
#     for phase in range(N - 1):
#         # t = min(numbers[phase, N]) # IM 시험 볼 때
#         minV = numbers[phase]
#         for idx in range(phase + 1, N):
#             if minV > numbers[idx]:
#                 minV = numbers[idx]
#                 minP = idx
#         numbers[minP], numbers[phase] = numbers[phase], numbers[minP]
#     return numbers
def asc_1(numbers, N):
    for i in range(N-1):
        min_p = i
        for j in range(i+1, N):
            if numbers[min_p] > numbers[j]:
                min_p = j
        numbers[i], numbers[min_p] = numbers[min_p], numbers[i]
    for num in range(len(numbers)):
        print(numbers[num], end=' ')
    return numbers


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{tc + 1}', end = ' ')
    asc_1(numbers, N)
    print() # 빈 줄 출력
