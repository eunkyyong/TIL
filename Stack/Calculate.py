
top = -1
stack = [0] * 100

icp = {'(':3, '*':2, '/':2, '+':1, '-':1}  # stack 밖에서의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}  # stack 안에서의 우선순위

fx = '(6 + 5 * (2 - 8) / 2)'
postfix = ''
for tk in fx:
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):  # 여는 괄호 push, top 원소보다 우선순위가 높으면 push
        top += 1  # push
        stack[top] = tk
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]: # 연산자이고 top 원소보다 우선순위가 높지 않으면
        while isp[stack[top]] >= icp[tk]:  # top 원소보다 우선순위가 낮을 때까지 pop
            top -= 1  # pop
            postfix += stack[top+1]
        top += 1  # push
        stack[top] = tk
    elif tk == ')':
        while stack[top] != '(':
            top -= 1  # pop
            postfix += stack[top+1]
        top -= 1  # 여는 괄호 pop해서 버림.
        stack[top + 1]
    else:
        postfix += tk
print(postfix)