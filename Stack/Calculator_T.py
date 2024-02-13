s = '(6+5*(2-8)/2)'
def step1():
    ST = []
    result = []
    # prio = {'+':1, '*':2, '-':1, '/':2, '(':100}
    icp = {'+':1, '*':2, '-':1, '/':2, '(':100}  # 스택 밖 우선순위
    isp = {'+':1, '*':2, '-':1, '/':2, '(':0}  # 스택 안 우선순위
    for c in s:
        if c.isdigit():
            result.append(c)
        elif c == ')':  #  왼쪽괄호 나올때까지 pop. 사람이 보기 편하게 괄호 붙이는거. 컴은 후위표기법으로 계산.
            while ST[-1] != '(':
                result.append(ST.pop())
            ST.pop()  # 괄호 나오기 전까지 것들을 result에 +

        else:
            if ST and isp[ST[-1]] < icp[c]:  # '('는 제일 먼저 st에 넣어주고, ')'이 나올때까지 우선순위 가장 낮게 하여 안나오게 한다. ')'이 나왔을 때 '('까지 뽑아낸다.
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]:  # st에 *있고 +을 처리할 때
                    result.append(ST.pop())
                ST.append(c)
    while ST:
        result.append(ST.pop())
    # print(result)
    return result

def step2(lst):
    ST = []
    for c in lst:  #피연산자
        if c.isdigit():
            ST.append(c)
        else:  # 연산자면 st에서 피연산자 2개 가져옴
            v2 = ST.pop()
            v1 = ST.pop()
            # t = calc(v1, v2, c)
            ST.append(calc(int(v1), int(v2), c))
    return ST.pop()

def calc(v1, v2, op):
    if op == '+':
        return v1+v2
    elif op == '-':
        return v1-v2
    elif op == '*':

        return v1*v2
    else:
        return v1//v2
post_order= step1()
# print(post_order)
print(step2(post_order))