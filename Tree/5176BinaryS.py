"""
3
6
8
15
"""
# inOrder
def inOrder(root):
    global vle
    if root <= N:
        inOrder(root * 2)
        TREE[root] = vle
        vle += 1
        inOrder(root * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    TREE = [0] * (N+1)
    vle = 1
    inOrder(1)
    print(f'#{tc} {TREE[1]} {TREE[N//2]}')

def inOrder(root):
    global vle
    if root<=N:
        inOrder(root*2)
        TREE[root] = vle
        vle += 1
        inOrder(root*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    TREE = [0] * (N+1)
    vle = 1
    inOrder(1)






