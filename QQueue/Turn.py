# def isFull():
#     return rear == N-1
#
# def isEmpty():
#     return front == rear
#
# def deQueue():
#     global front
#
#     if isEmpty():
#         print('empty')
#         return
#     front += 1
#     return Q[front]
#
# def enQueue(item):
#     global rear
#
#     if isFull():
#         print('full')
#         return
#     rear += 1
#     Q[rear] = item


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(M):
        lst.append(lst.pop(0))
    print(f'#{tc} {lst[0]}')

