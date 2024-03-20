def insert(value):
    global last
    last += 1
    TREE[last] = value  # 마지막 데이터 가리키고 있음

    c = last
    p = last//2
    while p >= 1 and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c//2
    print(TREE)

# 최대 힙의 데이터 pop하기
def pop():
    global last

    t = TREE[1]
    TREE[1] = TREE[last]
    last -= 1

    p = 1
    c = p*2
    while c <= last:          #TREE[c] != 1:
        if c+1<=last and  TREE[c] < TREE[c+1]:
            c += 1
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p*2
        else:
            break
    return t
TREE = [0, 20, 15, 19, 4, 13, 11] + [-1] * 100

last = 6
# insert(17)
# insert(23)
print(pop())
print(pop())


# def insert(value):
#     global last
#
#     last += 1
#     TREE[last] = value
#
#     c = last
#     p = c//2
#     while p>=1 and TREE[p] < TREE[c]:
#         TREE[p], TREE[c] = TREE[c], TREE[p]
#         c = p
#         p = c//2
#         print(TREE)
#
# def pop():
#     global last
#
#     t = TREE[1]
#     TREE[1] = TREE[last]
#     last -= 1
#
#     p = 1
#     c = p*2
#     while c<=last:     #TREE[c] != 1:
#         if c+1 <= last and TREE[c] < TREE[c+1]:
#             c += 1
#         if TREE[p] < TREE[c]:
#             TREE[p], TREE[c] = TREE[c], TREE[p]
#             p = c
#             c = p*2
#         else:
#             break
#
#     return t
#
# TREE = [0, 20, 15, 19, 4, 13, 11] + [-1] * 100
# # print(TREE)
# last = 6
# # insert(17)
# # insert(23)
# print(pop())
# print(pop())
