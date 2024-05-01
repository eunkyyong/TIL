N = int(input())

def decomposition_sum(number):
    result = number
    while number > 0:
        result += number % 10
        number //= 10
    return result


for i in range(max(1, N - 9 * len(str(N))), N):
    if decomposition_sum(i) == N:
        print(i)
        break
else:
    print(0)
