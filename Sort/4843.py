import sys
sys.stdin = open("/sample_input.txt", "r")

def getMax(phase): # selection sort 하는 함수 desc.
    maxi = Ai[phase]
    maxP = phase
    for i in range(phase+1, N):
        if maxi < Ai[i]:
            maxi = Ai[i]
            maxP = i
    return maxP

def getMin(phase): # selection sort 하는 함수 asc.
    mini = Ai[phase]
    minP = phase
    for j in range(phase+1, N):
        if mini > Ai[j]:
            mini = Ai[j]
            minP = j
    return minP


def selecSort(N):
    for phase in range(N-1):
        if phase%2 == 0: # 홀수 번째 인덱스일 때, getMax
            maxp = getMax(phase)
            Ai[maxp], Ai[phase] = Ai[phase], Ai[maxp]
        else:
            minp = getMin(phase)
            Ai[minp], Ai[phase] = Ai[phase], Ai[minp]
    return Ai

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    selecSort(N)
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(Ai[i], end=' ')
    print()

