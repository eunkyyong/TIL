def f(i, k):  # i 현재 위치, k 목표
    if i==k:
        print(brr)
    else:
        print(arr[i])
        f(i+1, k)

arr = [10, 20, 30]
N = len(arr)
brr = [0]*N
