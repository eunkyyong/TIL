def preOrder(root):
    if TREE[root]:
        print(root, TREE[root], end = ' ')
        preOrder(root * 2)
        preOrder(root * 2 + 1)


s = 'TEST 순회! 테스트'
lst = list(s)
N = len(lst)
TREE = [0] * 100
for idx in range(N):
    TREE[idx+1] = lst[idx]

# print(TREE)  # [0, 'T', 'E', 'S', 'T', ' ', '순', '회', '!', ' ', '테', '스', '트',

preOrder(1)  # 1 T 2 E 4 T 8 ! 9   5   10 테 11 스 3 S 6 순 12 트 7 회
