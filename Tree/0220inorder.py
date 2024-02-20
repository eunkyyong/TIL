import sys
sys.stdin = open("C:\cek\pycharm\TIL\Tree\input (11).txt", "r")
'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
def inOrder(root):
    if root:
        inOrder(leftC[root])
        print(st[root], end = '')
        inOrder(rightC[root])


T = 10
for tc in range(1, T+1):
    N = int(input())
    st = [0] * (N+1)
    leftC = [0] * (N+1)
    rightC = [0] * (N+1)
    for j in range(N):
        lst = list(input().split())
        # print(lst)
        p = int(lst[0])
        s = lst[1]
        st[j+1] = s
        for k in range(2, len(lst)):
            if leftC[p] == 0:
                leftC[p] = int(lst[k])
            else:
                rightC[p] = int(lst[k])
    print(f'#{tc}', end = ' ')
    inOrder(1)
    print()