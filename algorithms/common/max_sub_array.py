class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=nums[:]
        dp[0]=nums[0]
        m=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i], nums[i]+dp[i-1])
            m=max(m,dp[i])
        return m


    def maxSubArrayKadane(self, nums: List[int]) -> int:
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum