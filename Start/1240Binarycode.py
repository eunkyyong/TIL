# 바코드 라고 생각하면 됨
# 시작위치 어떻게 찾음? - 관건
# 이런 문제는 데이터 분석 우선. -- 여기선 모든 코드는 1로 끝남.
# dictionary - 8: 0110111 이런 식으로 만들어보기.
# 내일 풀어야 하는 문제 1242

mapping = {'0':'0001101', '1':'0011001', '2':'0010011', '3':'0111101', '4':'0100011',
           '5':'0110001', '6':'0101111', '7':'0111011', '8':'0110111', '9':'0001011'}
# ARR[row].index('1')
# ARR[row][::-1].index('1')
#
# s = '000010'
# print(s.index('1'))
# print(s[::1].index('1'))

#
import sys
sys.stdin = open("C:\cek\pycharm\TIL\Start\input (14).txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(N):
        ARR = [input() for _ in range(N)]
    # 암호코드 정보 출력 - 1이 나오는 곳부터?

    for row in range(N):
        if ARR[row].count('1'):
            # M = 코드의 시작 + 56(7bit * 8 numbers) + 뒤에 남은거
            # M = col + 56 + ARR[row][::-1].index('1')
            # 왼쪽 시작 위치
            col =
            break

    result = []
    for i in range(col, col+56, 7):
        code = ARR[row][i:i+7]
        result.append(mapping[code])
    # 홀수, 짝수만 체크하면 됨
    odd = []
    even = []
    for i in result:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    v1 = sum(odd) * 3
    v2 = sum(even)
    if (v1 + v2)%10 == 0:
        print(sum(result))
    else:
        print(0)