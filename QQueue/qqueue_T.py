# 다른 언어 위해 operator 구현해보자.
def isFull():
    return rear == SIZE-1

def isEmpty():
    return front == rear

def deQueue():
    global front

    if isEmpty():
        print('empty')
        return

    front += 1
    return Q[front]

def enQueue(item):
    global rear

    if isFull():
        print('full')
        return

    rear += 1
    Q[rear] = item



SIZE = 3
Q = [-1] * SIZE
front = -1
rear = -1
enQueue(10)
enQueue(20)
enQueue(30)
enQueue(40)
t = deQueue()
print(t)
print(deQueue())
print(deQueue())
