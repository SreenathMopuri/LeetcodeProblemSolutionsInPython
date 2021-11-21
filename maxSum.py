# Maximum Subarray
"""
pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix
leetcode link: https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(currSum, maxSub)
        return maxSub
        