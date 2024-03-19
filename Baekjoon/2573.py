arr = [10,20,30]
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

dfs([0]*N,[0]*N,0)
