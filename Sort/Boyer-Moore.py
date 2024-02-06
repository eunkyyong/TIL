# alphabet을 주면 숫자가 바로 나오게끔!
# ASCII 값 ?
# 모두 소문자로 가정
def make(p):
    M = len(p)
    jump = [M] * (ord('z')+1)
    # print(len(jump), jump)

    for i in range(M):
        c = p[i]
        jump[ord(c)] = M-1-i
        # 왜 좌표 구할 때 ord..., jump는 자료의 skip 배열인듯 47/60
        # rithm 문자열의 skip 배열 -> i가 증가할 때 감소함
        # print(jump[ord('m')])
        # print(jump[ord('r')])
    return jump

def find(p,t):
    M = len(p)
    N = len(t)

    ti = 0
    pi = M-1

    while ti+pi < N and pi>=0: # 실제 데이터가 있는 좌표: ti+pi
        if t[ti+pi] == p[pi]:
            pi -= 1
        else:
            pos = ord(t[ti+pi])
            ti += jump[pos]
            pi = M-1
    if pi < 0:
        return ti
    else:
        return -1

t = 'a pattern matching algorithm'
p = 'rithm'
jump = make(p)
# print(find(p, t))

# p = 'matw'
# jump = make(p)
# 앞에 빈거 0으로 차있을테니..
# make(p)
print(find(p, t))
