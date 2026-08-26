#memoization:
def fib(n, memo):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


n = int(input("Enter n: "))

memo = [-1] * (n + 1)

print("Fibonacci number =", fib(n, memo))

#tabulation:
def fib(n):
    dp = [0] * (n + 1)

    if n > 0:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Enter n: "))

print("Fibonacci number =", fib(n))