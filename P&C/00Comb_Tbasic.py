# print(list(range(1, 2)))  # 데이터 확인 위함
cnt = 0
def combi(k, start):
    global cntg
    cnt += 1
    if k == K:
        print(path)
        return

    for i in range(start, N-K+1+k):
        path[k] = i
        combi(k+1, i+1)
    return

N = 5
K = 3
path = [-1] * K
combi(0, 0)
# 안봐도 되는 것들 모두 잘라냄.