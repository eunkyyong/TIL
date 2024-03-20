'''
3
2 7
3 15
36 1007
'''
from collections import deque
def bfs(N, M):
    q = deque()
    q.append((N, 0))
    visited = [0] * 1000001
    visited[N] = 1

    while q:
        (now, cnt) = q.popleft()

        for ans in [now*2, now-10, now+1, now-1]:
            if 0<ans<=1000000 and visited[ans] == 0 :
                q.append((ans, cnt+1))
                visited[ans] += 1
                if ans == M:
                    return cnt+1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N, M)}')
