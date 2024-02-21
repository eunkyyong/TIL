import sys
sys.stdin = open("C:\cek\pycharm\TIL\Tree\sample_input (6).txt", "r")

def enqueue(data):
    global last
    c = last
    p = last//2

    if c%2 == 1:
        TREE[p] = TREE[c] + TREE[c-1]
        last -= 2
    else:
        TREE[p] = TREE[c]
        last -= 1
    return TREE

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0] * 100
    for _ in range(M):
        nodeNum, nodeV = map(int, input().split())
        TREE[nodeNum] = nodeV

    last = N
    while last>=1:
        enqueue(last)
    print(f'#{tc} {TREE[L]}')