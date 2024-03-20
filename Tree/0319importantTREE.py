s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
def insert(value):
    pos = 1
    while TREE[pos] != -1:
        if TREE[pos] > value:
            pos *= 2
        else:
            pos = pos*2+1
    TREE[pos] = value

def inOrder_old(rootP):
    if TREE[rootP*2] != -1:
        inOrder(rootP * 2)
    print(TREE[rootP])
    if TREE[rootP*2+1] != -1:
        inOrder(rootP*2 + 1)

def find(key):
    # 해당 수의 트리에서의 순서를 반환하고, 없으면 -1 반환하는 함수!
    # 보통 이런 문제 낼 적, 인덱스 찾으라고 하지 않음
    # 인덱스 구할 때 순차 탐색 O(n) -> O(logN)(이진 탐색 트리)
    # 같은 수는 모두 다른 값을 갖고 있어야 함.
    pos = 1
    # 값이 있는 동안 찾는다!!
    while TREE[pos] != -1:
        if TREE[pos] ==key:
            return pos
        if TREE[pos] < key:
            pos = pos*2 + 1
        else:
            pos *= 2
    # 없으면 -1
    return -1
def inOrder(rootP):
    if TREE[rootP] != -1:
        inOrder(rootP * 2)
        print(TREE[rootP])
        inOrder(rootP*2 + 1)

TREE = [-1] * 100
insert(9)
insert(12)
insert(15)
insert(4)
print(TREE)
inOrder(1)
print(find(9))
print(find(4))
print(find(7))
print(find(12))