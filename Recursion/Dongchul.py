# 순열
arr = [0,1,2]
N = len(arr)

#배열의 인덱스에 넣을 수 있는 요소 다넣어보기

def dfs(perm,check, idx):
    if idx == N:
        print(perm)
        return

    for i in range(N):
        #체크 된애는 안쓰기
        if not check[i]:
            perm[idx] = arr[i]
            check[i] = 1
            dfs(perm,check, idx+1)
            check[i] = 0
# 어떤 직원이 어떤일 할거냐?
# idx : 직원 번호
def solve(idx,rate,check):
    global max_rate

    if idx == N:
        if rate > max_rate:
            max_rate = rate
        return

    # idx 번 직원이 i번 일을 하는 경우
    for i in range(N):
        # arr[idx][i] 성공확률
        #다음직원이 할 일을 결정
        if not check[i]:
            check[i] = 1
            solve(idx+1, rate * arr[idx][i],check)
            check[`i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #퍼센트 > 실수
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j]/100
    max_rate = 0
    solve(0,1,[0]*N)
    print(f'#{tc} {max_rate*100:.6f}')