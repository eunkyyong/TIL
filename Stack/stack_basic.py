# def push(n):
#     global top
#     top += 1
#     if top == size:
#         print('Overflow!')
#     else:
#         stack[top] = n
#
#     top = -1
#     size = 10
#     stack = [0]*size
#
#     top += 1
#     stack[top] = 10
#
#     top += 1
#     stack[top] = 20
#
#     push(30)
#
#     while top>=0:
#         top -= 1
#         print(stack[top+1])
#########################################
def push(c):
    global top
    if is_full():
        print("Full!")
    top += 1
    STACK[top] = c

def pop():
    global top
    if is_empty():
        print('empty~')
        return
    top -= 1
    return STACK[top+1]

def peek():
    return STACK[top]
    # 현장에 가서는 STACK의 객체와, 이 함수들을 class로 묶어줘야 한다.

def is_empty():
    if top < 0:
        print('empty!')
        return True # 함수 이름이 is_empty이므로 boolean
    return False

def is_full():
    # 현재 상태가 full이면 못넣어
    if top == SIZE-1:
        print('full')
        return True
    return False

SIZE = 10
STACK = [0]*SIZE
top = -1  # 아직 아무것도 안넣었다!! 완전 오래된 자료구조
push('A')
push('B')
push('C')
c = pop()
print(c)
print(pop())
print(pop())