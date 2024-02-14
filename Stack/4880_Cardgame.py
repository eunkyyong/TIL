# 분할정복
# 많은 데이터 중 하나 선택.
# 처음 23(거의 중앙값) 잡으면, 왼쪽에 기준보다 작은 값, 오른쪽에 기준보다 큰 값으로 나누는 작업 Partitioning.
# partitioning 은 응용 때 함!!!!

# N = 6
# numbers = [68, 15, 23, 41, 44, 16]
#
# def quickSort(s, e):
#     # 재귀 빠져나올 조건
#     while s<e:
#         p = partition(s, e)
#         quickSort(s, p-1)
#         quickSort(p+1, e)
#
#
# quickSort(0, N-1)
#

def getWinner(w1, w2):
    # 가위바위보 게임 여기 있어야 함
    if s[w1] == 1:
        if s[w2] == 2:
            return w2
    if s[w1] == 1:
        if s[w2] == 3:
            return w1
    if s[w1] == 2:
        if s[w2] == 3:
            return w2
    if s[w1] == 2:
        if s[w2] == 1:
            return w1
    if s[w1] == 3:
        if s[w2] == 1:
            return w2
    if s[w1] == 3:
        if s[w2] == 2:
            return w1
    if s[w1] == s[w2]:
        if w1>w2:
            return w2
        else:
            return w1

# i~j 중 위너의 위치를 return
def game(i, j):
    if i == j:
        return i # 승자 한명
    
    # 재귀
    winner1 = game(i, (i+j)//2)
    winner2 = game((i+j)//2+1, j)
    return getWinner(winner1, winner2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = [0] + list(map(int, input().split()))
    print(f'#{tc} {game(1, N)}')