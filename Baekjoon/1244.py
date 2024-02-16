def m_switch(b):
    for num in range(1, N+1):  # 번호는 1부터 시작되니까
        if num % b == 0:
            st[num] = (st[num]+1)%2

def f_switch(a):
    # 여학생이 받은 숫자를 기준으로 스위치 상태 바꾸기
    st[a] = int(not st[a])
    # left right independantly




N = int(input())
st = [0] + list(map(int, input().split()))
st_no = int(input())
for _ in range(st_no):
    sex, card_no = map(int, input().split())
    if sex == 1:
        m_switch(card_no)
    elif sex == 2:
        f_switch(card_no)
print(*st)
