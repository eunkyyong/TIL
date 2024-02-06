# p가 t에 나타나면 t의 위치를 return
# 없으면 -1
def find(p, t):
    N = len(t)
    M = len(p)
    # 1. txt에서 시작위치:ti, p의 위치:pi
    for ti in range(N-M+1):
        for pi in range(M):
            if p[pi] != t[ti+pi]:
                break

        else:
            # M안거치고 찾았을 때
            return ti
    return -1

p = 'is'
t = 'This is a book'

print(find('iss', t))

def find_for(p,t):
    N = len(t)
    M = len(p)
    while ti<N and pi<M:
        if t[ti] == p[pi]:
            ti += 1
            pi += 1
        else:
            ti = ti-pi
            pi = 0 # pi-pi
            #'Thia'와 'This' 비교 시,
    # pi == M 이면 찾은거
    if pi==M:
        return ti-M # ti-pi
    else:
        return -1

def find_for(p,t):
    N = len(t)
    M = len(p)
    while ti<N and pi<M:
        if t[ti] != p[pi]:
            ti = ti - pi
            pi = -1
        ti += 1
        pi += 1
    if pi ==M:
        return ti-pi
    else:
        return -1
