def m_switch(b, C):
    for num in range(1, len(C)):
        if num % b == 0:
            C[num] = (C[num]+1) % 2


def f_switch(a, D):
    D[a] = 1-D[a]
    lf = a - 1
    rg = a + 1
    while lf >= 1 and rg <= len(D) and D[lf] == D[rg]:
        D[lf] = 1-D[lf]
        D[rg] = 1-D[rg]
        lf -= 1
        rg += 1


N = int(input())
st = [0] + list(map(int, input().split()))
st_no = int(input())
for _ in range(st_no):
    sex, card_no = map(int, input().split())
    if sex == 1:
        m_switch(card_no, st)
    elif sex == 2:
        f_switch(card_no, st)
st.pop(0)
for t in range(0, N//20+1):
    string = st[20*t:min(20*(t+1), N)]
    print(*string)
