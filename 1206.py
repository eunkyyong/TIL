# 1일차 View - 어떤 문제든 2시간 이상은 고민해봐야 한다.
# 하루 이틀 잊어버리고 다시 풀어봐야 한다.
# 파일을 직접 읽어들이기 TC = Testcase
import sys
sys.stdin = open("1206input.txt", "r") # SWEA site에 올릴 때는 위 두줄 없애고.
TC = 10
for tc in range(1, TC+1):
    N = int(input())
    BUILD = list(map(int, input().split()))
    print(N, BUILD)# 선생님은 입력받은 다음에 이 상수를 변경안할거면 대문자로 씀.

# cnt = 0
#     # N개의 높이가 주어진다. N개를 재배열해야하므로
#     # 제일 큰 값 - 두번째 큰 값 +1 개는 조망권 확보. 하지만 식을 따로 만들기 힘들다..
#     # cnt += arr1[-1] - arr1[-2] + 1
#     # arr[i] 전후 2개씩 비교.
# for i in range(len(arr)):
#     for j in range(-2, 2):
#         if -2 <= j <0:
#             if arr[i-j] < arr[i]:
#                 pass
#         elif 0< j <= 2:
#             if arr[i+j] < arr[i]:
#                 cnt += 1
# return cnt
