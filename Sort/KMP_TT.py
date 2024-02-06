def make(p):
    M = len(p)
    j = 0
    for i in range(1, M): # 0은 -1부터 갈거니까..? 1부터 시작..?
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0

def find(p,t):
    N = len(t)
    M = len(p)
    ti = pi = 0 # 시작 위치
    while ti<N and pi<M:
        if pi == -1 or t[ti] == p[pi]:
            ti += 1
            pi += 1
        else:
            pi = lps[pi]
            # ti는 돌아갈 필요가 없음
    if pi == M:
        return ti-pi
    else:
        return -1
            
t = 'zzabcdabcefgg'
p = 'abcdabcef'
# KMP: 이미 비교했던 거는 비교 다시 안했음 좋겠어!
# table을 먼저 만들어야 함!
lps = [-1] * len(p)
make(p)
# print(lps) # lps는
print(find(p, t))
print(find('abcdaa', t))