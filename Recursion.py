# 재귀함수, 피보나치함수
# dp 포함


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


print(fibo(6), dp_fibo(6))
