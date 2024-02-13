# 백트래킹 이용하여 순열 구하기
def backtrack(a, k, input):
    global Maxcandidates
    c = [0] * Maxcandidates

    if k == input:
        for i in range(1, k+1):
            print(a[i], end = " ")
        print()  # process_solution(a, k) 으로 위 세줄 요약할 수 있음??
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm = [False] * Nmax

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates