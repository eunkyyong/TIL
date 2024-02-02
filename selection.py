# 데이터를 정렬한 후 정렬 결과를 리스트로 return 46/57 이해감!!
def selectionS(numbers):
    N = len(numbers)
    # phase=0: 0에서 N-1중 제일 작은 값의 위치를 찾아서 0번째와 교환
    # phase=1: 1에서 N-1중 제일 작은 값의 위치를 1번째와 교환
    # phase=2: 2에서 N-1중 제일 작은 값의 위치를 2번째와 교환
    # N=5이면 phase 3
    for phase in range(N-1):
        # t = min(numbers[phase, N]) # IM 시험 볼 때
        minV = numbers[phase]
        for idx in range(phase+1, N):
            if minV > numbers[idx]:
                minV = numbers[idx]
                minP = idx
        numbers[minP], numbers[phase] = numbers[phase], numbers[minP]
    return numbers

# 똑같은 코드
    # for phase in range(N-1):
    #     # t = min(numbers[phase, N]) # IM 시험 볼 때
    #     minV = phase
    #     for idx in range(phase+1, N):
    #         if numbers[minP] > number[idx]:
    #             minP = idx
numbers = [64, 25, 10, 22, 11]
selectionS(numbers)
print(selectionS([64, 25, 10, 22, 11, -2]))
# print(selectionS([64, 25, 10, 22, 11, -2]))
# print(selectionS([64, 25, 10, 22, 11, -2]))
