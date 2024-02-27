def step1():   # in-coming priority : 중위표현식, in-stack priority : 후위 표현식
    st = []
    result = []
    icp = {'+':1, '*':2, '-':1, '/':2, '(':100} # stack 밖 우선순위
    isp = {'+':1, '*':2, '-':1, '/':2, '(':0}  # stack 안 우선순위
    for c in s:
        if c.isdigit():
            result.append(c)
        elif c == ')':
            while st[-1] != '(':
                result.append(st.pop())
            st.pop()

        else:
            if st and isp[st[-1]] < icp[c]