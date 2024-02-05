import sys
sys.stdin = open("/aaaa/input_w.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    # 가로 세로
    N, K = map(int, input().split())
    # N*N array, K = length of the word
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] # 0을 넣어서 조건문 한번 덜 씀
    arr += [[0]*(N+1)]
    N += 1
    # white -1 에 단어가 들어갈 수 있음. K 와 N(연속된1의 개수)
    # 그림보니까 세로에도 들어갈 수 있는 듯
    # 일단 가로부터, 아까랑 달리 list로 받음, type:int..
    # 연속된 1지점 >= K, cnt += 1 (가로, 세로 모두다 ..) arr에 1 지점 나와있음
    cnt_word = 0
    cnt_one = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                cnt_one += 1
            else:
                if K == cnt_one:
                    cnt_word += 1
                cnt_one = 0
                # 3 < 5, 4, 5번째도 빼줘야함 -> 그래서 K==cnt_one 만 조건문 붙힘.

    for c in range(N):
        cnt_one = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt_one += 1
            else:
                if K == cnt_one:
                    cnt_word += 1
                cnt_one = 0
    print(f'#{tc} {cnt_word}')



