def insert(data):
    idx = 1
    while TREE[idx]:  # 빈 노드 나타날 때까지 찾아가기, 트리에 데이터가 있는 동안
        # 아직 트리에 안들어간 것 아닌가...
        if TREE[idx] > data:
            idx *= 2
        else:
            idx = idx*2 + 1
    TREE[idx] = data
    print(TREE)

# 찾으면 idx, 못찾으면 -1
def find(key):
    idx = 1
    while TREE[idx]:
        if TREE[idx] == key:
            return idx
        if TREE[idx] < key:
            idx = idx * 2 + 1
        else:
            idx *= 2
    return -1

TREE = [0] * 100
for data in [9, 4, 12, 3, 6, 15, 13, 17]:
    insert(data)

print(find(2))
print(find(16))
print(find(5))
print(find(3))
print(find(12))
print(find(15))
