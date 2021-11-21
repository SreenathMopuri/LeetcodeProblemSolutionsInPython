# Two Sum Problem
"""
use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice;
Leetcode link: https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val:idx
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[val] = i
