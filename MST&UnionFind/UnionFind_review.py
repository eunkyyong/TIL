#x가 포함된 그룹의 대표 반환하는 함수
def find_set(x):
    if x==p[x]:
        return p[x]
    return find_set(p[x])
#x와y의 그룹을 통합
def union(x,y):
    r1 = find_set(x)
    r2 = find_set(y)
    if r1 == r2:
        return
    if r1 < r2:
        p[r2] = r1
    else:
        p[r1] = r2

#전체 그룹의 개수를 반환하는 함수
def solve():

    for i in range(0,M*2,2):
        union(data[i], data[i+1])

    #전체 학생들의 대표자의 수를 세면 그룹의 개수
    group_set = set()   #그룹의 대표자를 넣는 set
    for i in range(1,N+1):
        group_set.add(find_set(i))

    return len(group_set)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    p = [x for x in range(N+1)]

    result = solve()
    print(f'#{tc} {result}')
