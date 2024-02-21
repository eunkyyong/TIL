def enqueue(data):
    global last
    last += 1
    TREE[last] = data

    c = last
    p = last//2

    while p and TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c // 2
    return TREE

def dequeue():
    global last
    result = TREE[1]
    TREE[1] = TREE[last]  # 루트로 옮기고
    last -= 1  # 노드 없애줌

    p = 1
    c = p*2  # 왼쪽 기준으로 두고 오른쪽만 (양쪽 조건문 싫어서)
    while c <= last:  # 인덱스 변화가 생길 땐, 값 비교 전에 범위 비교부터!!!
        if c+1<=last and TREE[c] < TREE[c+1]:
            c += 1  # c가 2개면 그 중 큰 c를 p와 비교해야 함
        if TREE[c] > TREE[p]:
            TREE[p], TREE[c] = TREE[c], TREE[p]  # 값 바꿔주고
            p = c  # c올려줬으니 c, p 인덱스도 바꿔줘야 함.
            c = p*2
        else:
            break
    print(last, TREE)
    return result

TREE = [0] * 100
last = 0
for data in [20, 15, 19, 4, 13, 10]:
    enqueue(data)

if last:  # last node 안 값의 존재 유무
    print(dequeue())
    print(dequeue())
    print(dequeue())