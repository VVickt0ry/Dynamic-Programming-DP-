class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1) # dp[i] 表示前i个房子能偷到的最大金额
        if n == 1 :
            return nums[0]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-2],dp[i-3]) + nums[i]
        return max(dp[n-2], dp[n-1])