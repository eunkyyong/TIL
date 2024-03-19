def partial(k, subSum, rSum):
    if subSum > 10:
        return
    if subSum + rSum < 10:
        return

    if subSum == 10:
        print(result.count(1))
        print(result)
        return
    if k==N:
        return
    # K번째 원소가 포함되지 않은 거야
    result[k] = 0
    # 포함안되어있으니까 그냥 subsum 내려줘
    partial(k+1, subSum, rSum-numbers[k])
    result[k] = 1
    # 부분집합의 합이야 내려올 때마다 그 값을 더해줘!
    # k번째 원소의 값을 더해줘!
    partial(k+1, subSum + numbers[k], rSum-numbers[k])
    # 보통 안써서 그렇지, 있음!!
    return

numbers = [i for i in range(1, 11)]
# numbers = [8, 1, 9, 7, 2, 5]
N = len(numbers)
result = [-1] * N
partial(0, 0, sum(numbers))