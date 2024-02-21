'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

def enq(data):
    global last
    last += 1
    TREE[last] = data

    c = last
    p = last//2

    while p and TREE[p]>TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c//2
    return TREE

def anc(M):
    vl = 0
    # data = TREE[M]
    while M//2>=1:
        vl += TREE[M//2]
        M = M // 2
    return vl

T = int(input())
for tc in range(1, T+1):
    TREE = [0] * 1000000
    last = 0
    N = int(input())
    s = list(map(int, input().split()))
    for i in s:
        enq(i)
    a = anc(N)
    print(f'#{tc} {a}')