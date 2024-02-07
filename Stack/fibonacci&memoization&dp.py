def fibo_r(n):
    if n<2:
        return n

    return fibo_r(n-1) + fibo_r(n-2)

print(fibo_r(7))  # 13
#######################Memoization############
n = 7
memo = [0] * (n+1)  # 5까지 만들어야 하므로
memo[0] = 0
memo[1] = 1
def fib_m(n):
    if n>1 and memo[n] == 0:
        memo[n] = fib_m(n-1) + fib_m(n-2)
        return memo[n]
    else:
        return memo[n]

print(fib_m(n))  # 13
##############DP
dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
########A형 전까지는 이거 안써도 됨##########

