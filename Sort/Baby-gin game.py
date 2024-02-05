# 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin이라고 부른다.
# Exaustive Search(Brute-force or generate-and-test)
# 모든 경우의 수 생성, 6자리 수 6팩토리얼
# 앞 3자리, 뒤 3자리 잘라 run인지 triplet인지 확인.

#Baby gin 을 완전검색 아닌 방법으로 풀어보자.
# 단순수열 모든 수 구하면 너무 노가다임..
# triplet 찾고 run 찾기! 그럼 경우의 수 많이 줄어들어서 가능할 듯
# triplet 먼저 찾기
if i in str:
    if i # 3n in str:
        # counting sort 연습
        N = 6
        K = 9  # 0~K
        data = [7, 2, 4, 5, 2, 3]  # 0~9
        counts = [0] * (K + 1)
        temp = [0] * N  # 빈배열
        # count 배열에 기록하기
        for x in data:
            counts[x] += 1
        # count 누적합 구하기
        for i in range(1, K + 1):
            counts[i] += counts[i - 1]
            # 누적합에서 해당 숫자 -3
# -------------------
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run +tri == 2: print("Baby Gin")
else: print("Lose")
#--------------------------------
# DATA = [0, 4, 1(1), 3, 1(2), 2, 4, 1(3)]
# TEMP = [0, 1(1), 1(2), 1(3), 2, 3, 4, 4]
# 1(1)이 앞에 있으므로 앞에 있는 걸 유지하면서 변경(최소 변경)
K = 4+1 # DATA에 있는 것중 가장 큰 값+1, 누적합 칸의 개수 0~가장 큰 값
N = len(DATA)
COUNTS = [0]*K
for d in DATA:
    COUNTS[d] += 1 #누적한 것

for i in range(1, K):
    COUNTS[i] = COUNTS[i] + COUNTS[i-1]
print(COUNTS) #누적 위치 배열 만듦

TEMP = [-1] * N # 내 결과 넣을 곳. -1을 쓴 이유는, 0,1넣으면 헷갈릴 수 있음, 그래서 안쓰는 data로 초기화.
for i in range(N-1, -1, -1): # 0이 포함되어야 함.
    d = DATA[i]
    idx = COUNTS[d] - 1
    TEMP[idx] = d
    COUNTS[d] -= 1
print(TEMP)

#----------------------------------------
# DATA = [0, 4, 1, 3, 1, 2, 4, 1] # [-1, -1, -1, -1, -1, -1, -1, -1] 넣기 별로 안좋음
# # DATA[7] => DATA[N-1] => 1
# COUNTS= [1, 4, 5, 6, 8] # 누적. 마지막의 다음위치 나타냄(인덱스) 0, 1, 2, 3, 4
# # DATA[6] => DATA[N-2] => 4
# TEMP =[-1, -1, -1, -1, 2, -1, -1, 4]
#
#
# COUNTS = [0] * 5 # count해야 되니 0으로 초기화해준다. 칸 개수만큼!! [0]*(K+1) K:data에 있는 것중 가장 큰 값