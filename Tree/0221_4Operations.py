import sys
sys.stdin = open("C:\cek\pycharm\TIL\Tree\input (13).txt", "r")
def postOrder(root):
    if TREE[root][0] not in ['+', '-', '*', '/']:  # 숫자면
        return TREE[root][0]
    else:
        v1 = float(postOrder(int(TREE[root][1])))
        v2 = float(postOrder(int(TREE[root][2])))
        if TREE[root][0] == '+':
            value = v1 + v2
        elif TREE[root][0] == '-':
            value = v1-v2
        elif TREE[root][0] == '*':
            value = v1 * v2
        else:
            value = v1 // v2
        TREE[root][0] = str(value)
        return int(value)

T = 10
for tc in range(1, T+1):
    N = int(input())
    TREE = [[] for _ in range(N+1)]
    for _ in range(N):
        lst = input().split()
        no = int(lst[0])
        TREE[no] = lst[1:]
    print(f'#{tc} {postOrder(1)}')
