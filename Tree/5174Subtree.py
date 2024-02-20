'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''
def inOrder(root):
    global vle
    if root:
        inOrder(leftC[root])
        # print(root)
        inOrder(rightC[root])
        vle += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    leftC = [0] * (E+2)
    rightC = [0] * (E+2)
    for i in range(0, 2*E, 2):
        # 부모, 자식 노드 쌍
        p = lst[i]
        c = lst[i+1]
        if leftC[p] == 0:
            leftC[p] = c
        else:
            rightC[p] = c
    vle = 0
    inOrder(N)
    print(f'#{tc} {vle}')