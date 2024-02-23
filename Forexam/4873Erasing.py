'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
'''
T = int(input())
for tc in range(1, T+1):
    st = []
    lst = list(input())
    item = lst.pop(0)
    st.append(item)
    while lst:
        item = lst.pop(0)
        if st and item == st[-1]:
            st.pop()
        else:
            st.append(item)
    print(f'#{tc} {len(st)}')




