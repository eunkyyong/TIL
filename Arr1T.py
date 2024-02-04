N = int(input())
arr = list(map(int, input().split()))

'''9
7 4 2 0 0 6 0 7 0 
'''

max_v = 0 # 가장 큰 낙차
for i in range(N-1):
    cnt = 0 # 오른쪽에 있는 더 높은
    for j in range(i+1, N):
        if arr[i]>arr[j]: # 빈 칸을 통과한다!= 낙하한다!
            cnt += 1

    if max_v < cnt:
        max_v = cnt
print(max_v)
