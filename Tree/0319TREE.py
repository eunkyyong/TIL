s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
l = list(map(int, s.split()))
N = 13
TREE = [[] for _ in range(N+1)]
for i in range(0, len(l), 2):
    p = l[i]
    c = l[i+1]
    TREE[p].append(c)
print(TREE)

# preOrder(1)
def preOrder(root):
    print(root)
    # 길이 기준
    if len(TREE[root]):
        preOrder(TREE[root][0])
    if len(TREE[root])>1:
        preOrder(TREE[root][1])