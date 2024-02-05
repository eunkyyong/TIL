T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    ARR = list(map(int, input().split()))


    def solve(N, K, ARR):
        curP = 0
        pre = 0
        result = 0
        for _ in range(K):
            jump = ARR[curP]
            if ARR[curP] > 0 and pre < 0:
                jump = jump + (-pre)
            pre = ARR[curP]
            curP = curP + jump
            if curP < 0 or N-1 < curP:
                return result
            result = result + ARR[curP]
        return result


    print(f'#{tc} {solve(N, K, ARR)}')
