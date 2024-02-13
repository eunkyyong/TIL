# 중복조합으로 원소 3개를 뽑는 부분집합을 구해라.
# 재귀
N = 3
result = [-1] * N  # 0부터 데이터가 들어가기 때문
# c 배열에 후보를 만들어서 개수를 return
numbers = [23, 42, 15]
def construct_candidates(k, c):  # 가로로
    # 가지 칠 가지를 만들어주는 작업! 후보군을 만들자! 후보군의 모양에 따라 달라짐
    c[0] = 0
    c[1] = 1
    return 2 # 개수

def process_solution():
    print(result)
    for i in range(N):
        if result[i]:
            print(numbers[i], end = ' ')
    print()


def recur_g(k):  # k= depth
    if k == N:
        process_solution()
        return

    c = [-1] * 100
    nC = construct_candidates(k, c)  # 후보를 만들어줘!!
    for i in range(nC):
        result[k] = c[i]
        recur_g(k+1)
recur_g(0)