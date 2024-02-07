# 왼쪽 괄호가 나오면 잘 보관해 놓고, 오른쪽 괄호가 나오면 짝을 지어 throw it in버린다.
STACK = []
for c in s:
    if c == '(':
        STACK.append(c)
    elif c==')':
        if len(STACK) == 0:
            result = False
            break
        else:  # 넣기 전에 원래 stack에 있던 애 빼고 그 뺀 item이랑 비교해서 짝꿍이면 아무 조치 안취함!!
            temp = STACK.pop()
            if temp == '(':
                continue

        # if len(STACK) == 0 or STACK.pop() != '(':
        #     result = False
        #     break
        # 어차피 STACK 비었으니 아무것도 안하면 된다! c에 어느 행동을 취하기 전에
        # 비교해서 아무 행동 안취했으니!!! (STACK에 저장할 필요조차 없다.)
if len(STACK)>0:
    result = False

