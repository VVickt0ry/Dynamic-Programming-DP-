class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)  # 创建长度为n+1的数组来存储每个斐波那契数
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]