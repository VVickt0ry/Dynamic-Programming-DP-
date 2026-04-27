class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums) # 数组的最大长度不超过列表的最大值
        dp = [0] * (n+1)
        for num in nums:
            dp[num] += num # 将每个数出现的次数乘以数值本身，累加到对应位置
                           # 变相统计了数字出现的总和

        # 现在问题转化为打家劫舍问题
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        return max(dp[n], dp[n-1])