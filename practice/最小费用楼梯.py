class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        # 状态转移：爬到i阶的最小花费 = 前 1 阶 或 前 2 阶的最小花费 + 当前阶花费
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[n-1], dp[n-2])
        # 涉及到索所以有n-1和n-2





# 第二种解法
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
     n = len(cost) 
     dp = [0,0]
     for i in range(2, n+1):
        a = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])  
        dp.append(a)
     return dp[n]
        # dp[i]表示到达第i阶楼顶的最小花费，不包括第i阶的花费
        # 当前阶的最小花费 = 前1阶或前2阶的最小花费 + 当前阶花费
        # 最后返回dp[n]，即爬到第n阶的最小花费