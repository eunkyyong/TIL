# Heap 쓰는 이유 - 우선순위 큐 만들 때~!! 우선순위 높은 애가 먼저 빠질 때.
def enqueue(data):
    global last

    last += 1
    TREE[last] = data

    c = last
    p = last//2

    # while p:
    #     if TREE[p] < TREE[c]:
    #         TREE[p], TREE[c] = TREE[c], TREE[p]
    #         c = p
    #         p = c//2  # 순서바뀌지 않게 조심
    #     else:
    #         break
    # print(TREE)

    while p and TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c // 2
    print(TREE)

TREE = [0] * 100
last = 0
for data in [20, 15, 19, 24, 22]:
    enqueue(data)