def deq():
    global last
    tmp = h[1]
    h[1] = h[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and h[c] < h[c+1]:
            c+= 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp

N = 10  # 필요한 노드 수
h = [0] * (N+1)  # 최대 힙
last = 0  # heap의 마지막 노드 번호  // 우선순위 큐??
deq(2)
deq(5)
deq(3)
deq(6)
deq(4)
while (last>0):
    print(deq())
