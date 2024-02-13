# 각 원소가 부분집합에 포함되었는 지를 loop이용하여 확인하고 부분집합 생성하는 방법
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)
# 재귀는 변수 값만 바꿔도 계산 가능한 장점..?

```
bit = [0, 0, 0, 0]
# f(i, k) : bit[i]에 1or0을 채우는 함수
```

def backtrack(a, k, input):
    global Maxcandidates
    c = [0] * Maxcandidates

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2
Maxcandidates = 2
Nmax = 4
a = [0] * Nmax
backtrack(a, 0, 3)