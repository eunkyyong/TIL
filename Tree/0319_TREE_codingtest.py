arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 코테에서는 간단하게
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

# 자식이 없다는 걸 표시하기 위해 None
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def inorder(nodeNum):
    if nodeNum == None:
        return

    # 왼쪽으로 갈 수 있다면 진행
    inorder(nodes[nodeNum][0])
    print(nodeNum, end=' ')
    # 오른쪽으로 갈 수 있다면 진행
    inorder(nodes[nodeNum][1])
    # 저장을 해놨기 때문에, 왼쪽, 오른쪽이 index로
inorder(1)