from collections import deque

# q = deque()
# q.append(1)
# q.append(2)
# print(q.popleft())
# print(q.popleft())

q = []
for i in range(10000):
    q.append(i)
print('append')  # 어떤 단계인 지 표시하고자
while q:
    q.pop(0)
print('end')

dq = deque()
for i in range(20000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')