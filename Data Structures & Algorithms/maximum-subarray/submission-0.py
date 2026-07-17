class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        total = 0
        for i in range(len(nums)):
            if total < 0:
                total = 0
            total += nums[i]
            maxSum = max(maxSum, total)
        return maxSum