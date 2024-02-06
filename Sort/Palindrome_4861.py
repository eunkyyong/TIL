import sys
sys.stdin = open("C:\cek\pycharm\TIL\Sort\sample_input_4861.txt", "r")

# s가 회문이면 True, 아니면 False
def is_p(s):
    if s == s[::-1]:
        return True
    else:
        return False

def solve():
    # for M in range(N, 2, -1): 회문2
    for row in range(N):
        for col_s in range(N - M + 1):
            new_s = arr[row][col_s:col_s + M]
            if is_p(new_s):
                return new_s
    for col in range(N):  # col대로 안돎. 반복문 써야 함.
        for row_s in range(N- M +1):
            strr = ''
            # for num in range(M):
            # new_s = arr[row_s:row_s + M][col] 이렇게 안됨!!
            # 행에서 한 문자씩 가져오기
            for num in range(M):
                strr += arr[row_s+num][col]
            new_s = strr
            if is_p(new_s):
                return new_s
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)] # list로 바꾸는 건 list 내의 데이터를 바꾸고 싶을 때만.
    print(f'#{tc} {solve()}')

# #------------------------------------
# for i in range(N):
#     for j in range(N-M+1):
#         new_s = arr[i][j:j+M]
#         if is_p(new_s):
#             return new_s
#
#         new_s = ''
#         for row in range(j, j+M):
#             new_s += arr[row][i]
#         if is_p(new_s):
#             return new_s