# N = 10
# q = [0] * 10
# front = rear  = 1
# rear += 1
# q[rear] = 10
# rear += 1
# q[rear] = 20
# rear += 1
# q[rear] = 30
# while front!=rear:  # queue가 비어있지 않으면
#     front += 1  # dequeue()
#     print(q[front])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    prio = list(map(int, input().split()))






    # 현재 N개 중 M위치에 있는 문서를 중요도 prio 순서대로 뽑을 때, 몇 번째로 뽑히는 지?
    # prio[M] 의 중요도 숫자가 제일 큰 숫자부터 얼마나 떨어져 있는 지
    # prio sort
# enQueue(item)
# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# # 시간 복잡도는 매우 안좋지만...
# while queue:
#     print(queue.pop(0))