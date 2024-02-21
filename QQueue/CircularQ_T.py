Q =[]
Q.append(10)
if Q:
    print(Q.pop(0))

# 다른 언어 위해 operator 구현해보자.
def isFull():
    return front == (rear+1)%SIZE


def isEmpty():
    return front == rear


def deQueue():
    global front

    if isEmpty():
        print('empty')
        return

    front = (front + 1) % SIZE
    return Q[front]


def enQueue(item):
    global rear

    if isFull():
        print('full')
        return

    rear = (rear+1)%SIZE
    Q[rear] = item


SIZE = 4
Q = [-1] * SIZE
front = 0
rear = 0
t = deQueue()
print(t)
enQueue(10)
print(deQueue())
enQueue(20)
print(deQueue())
enQueue(30)
print(deQueue())
enQueue(40)
print(deQueue())
