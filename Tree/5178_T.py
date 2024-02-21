import sys
sys.stdin = open("C:\cek\pycharm\TIL\Tree\sample_input (6).txt", "r")

def postOrder(root):
    # 이런 식으로 누적시키기 위함도 있다
    if root*2 <= N:  # 의미는 없지만 가독성 위함
        TREE[root] += postOrder(root*2)
    if root*2+1 <= N:
        TREE[root] += postOrder(root*2+1)

    return TREE[root]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0] * (N+1)
    for _ in range(M):
        nodeNum, nodeV = map(int, input().split())
        TREE[nodeNum] = nodeV
    postOrder(1)
    print(f'#{tc} {TREE[L]}')