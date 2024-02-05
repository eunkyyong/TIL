# counting sort 연습
N = 6
K = 9 # 0~K
data = [7, 2, 4, 5, 2, 3] # 0~9
counts = [0] * (K+1) # 0-9까지 K+1의 숫자 배열에 각 숫자가 몇개씩 있는 지 기본 cnt 배열 만들기, 근데 맘대로 N개 만들어도 되지 않나?
temp = [0] * N # 빈배열
# count 배열에 기록하기
for x in data:
    counts[x] += 1
# count 누적합 구하기
for i in range(1, K+1):
    counts[i] += counts[i-1]
# data의 마지막 원소부터 정렬하기..
for i in range(N-1, -1, -1): # N-1 -> 0번 인덱스
    counts[data[i]] -= 1 # 개수를 인덱스로 변환(남은 개수 계산) # ???????? 여기선 data[i] 가 int라 가능..
    temp[counts[data[i]]] = data[i] # temp에 새로 대입
print(*temp)
#---------------

for x in data:
    counts[x] += 1
for i in range(1, K+1):
    counts[i] += counts[i-1]
for i in range(N-1, -1, -1):
    counts[data[i]] -= 1 # data 의 마지막 요소부터 누적합에서 -= 1 해주고 배치.
    temp[counts[data[i]]] = data[i] # 누적합이 곧 요소의 순서대로 정렬 시 위치라서.

# 구현 예시
num = 456789
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
for i in range(6): # while num>0: 몇자리 수인 지 모를때
    c[num%10] += 1 # 각 자리 수를 알아내기 위함
    num //= 10
