def enq(n):
    global last
    last += 1       # 마지막 노드 추가 (완전 이진트리 유지)
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # parent > child
    p = c//2        # 부모 번호 계산
    while p >= 1 and h[p] < h[c]:  # 부모가 있는데 더 작으면
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c//2  # (모두 노드 번호 가리킴.)

N = 10  # 필요한 노드 수
h = [0] * (N+1)  # 최대 힙
last = 0  # heap의 마지막 노드 번호  // 우선순위 큐??

enq(2)
enq(5)
enq(3)
enq(6)
enq(4)