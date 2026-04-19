
# 标准数组DP解法，空间换时间，逻辑直白、调试修改方便
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)  # 创建长度为n+1的数组来存储每个台阶的爬法数量
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]



# 第二种解法：滚动数组优化空间复杂度
# 思考:计算第i阶，永远只需要前2个结果dp[i-1]和dp[i-2]，更早的值完全没用
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # 只保留前两个状态，不再开数组
        a, b = 1, 2 
        for _ in range(3, n+1):
            c = a + b # 当前台阶总数
            a = b     # 状态向前滚动
            b = c
        return b


