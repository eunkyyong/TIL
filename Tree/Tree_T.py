'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def postOrder(root):
    if len(TREE[root]) >= 1:
        postOrder(TREE[root][0])
    if len(TREE[root]) >= 2:
        postOrder(TREE[root][1])
    print(root)

def preOrder(root):
    print(root)
    # l = TREE[root][0]
    # r = TREE[root][1]
    if len(TREE[root]) >= 1:
        preOrder(TREE[root][0])
    if len(TREE[root]) >= 2:
        preOrder(TREE[root][1])

N = int(input())
lst = list(map(int, input().split()))
TREE = [[] for _ in range(N+1)]

for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]

    TREE[p].append(c)
# print(TREE) index 가 parent node.
# [[], [2, 3], [4], [5, 6], [7], [8, 9], [10, 11], [12], [], [], [], [13], [], []]

postOrder(1)

#

