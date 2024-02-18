def m_switch(b):
    for num in range(1, len(st)):
        if num % b == 0:
            st[num] = (st[num]+1)%2

def f_switch(a):
    st[a] = int(not st[a])
    for lf in range(1, a, -1):
        for rg in range(a+1, len[st]):
            if st[lf] == st[rg]:
                st[lf] = int(not st[lf])
                st[rg] = int(not st[rg])
    # for i in range(0, a):
    #     lf = a-i
    #     # rg in range(a, N)
    #     rg = a+i
    #     if st[lf] == st[rg]:
    #         lf = int(not lf)
    #         rg = int(not rg)

N = int(input())
st = [0] + list(map(int, input().split()))
st_no = int(input())
for _ in range(st_no):
    sex, card_no = map(int, input().split())
    if sex == 1:
        m_switch(card_no)
    elif sex == 2:
        f_switch(card_no)
st.pop(0)
print(*st)
