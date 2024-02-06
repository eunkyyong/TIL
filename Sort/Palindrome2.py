import sys
sys.stdin = open("/Users/eunkyyong/PycharmProjects/pythonProject/TIL/Sort/input_palin.txt", "r")
def is_p(s):
    # chr(printf(%d,'A'))??????
    if s == s[::-1]:
        return True
    # 'ABA'
    if s.split(sep= 'A' or 'B' or 'C', 1)[0] == s.split(sep= 'A' or 'B' or 'C', 1)[1]:
        return True
    # str이 모두 한 문자로 되어있는 가? 'A' 같은 문자끼리는 모두 가능
    # str이 어떤 문자로 이뤄져 있는 지?...
    cnt = 0
    for c in s:
        if c == 'A':
            cnt += 1
    if cnt == len(s):
        return True
    cnt = 0
    for c in s:
        if c == 'B':
            cnt += 1
    if cnt == len(s):
        return True
    cnt = 0
    for c in s:
        if c == 'C':
            cnt += 1
    if cnt == len(s):
        return True

def solve():
    # 0 < M <=100, for문으로 M 범위지정???
    # 가장 긴 회문의 길이 구하기.
    # 아래 코드들은 가로, 세로 length M에 맞춰 탐색 후, 회문 체크
    # 이번에는,,, 저렇게 함 안됨. 조건 없어서 경우 너무 많음
    # 이번에는 회문 먼저 체크 후 100*100 내에 있는 지 확인?
    # for M in range(N, 2, -1): 회문2
    # N-1~3????까지 M (회문의 길이) 구하는 구문. 길이 모두 완전 탐색.
    # 여기서 N = 100, 의미상으론 N-1~1까지 구하는 거인 듯
    N = 100
    for M in range(N, 2, -1):
        for row in range(N):
            for col_s in range(N-M+1):
                new_s = arr[row][col_s:col_s+M]
                if is_p(new_s):
                    return len(new_s)
    for M in range(N, 2, -1):
        for col in range(N):
            for row_s in range(N-M+1):
                strr = ''
                for num in range(M):
                    strr += arr[row_s+num][col]
                new_s = strr
                if is_p(new_s):
                    return len(new_s)
    return -1

T = int(input())
for tc in range(1, T+1):
    arr = [input().strip() for _ in range(100)]
    print(f'#{tc} {solve()}')
