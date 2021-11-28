# 268. Missing Number
"""
leetcode link: https://leetcode.com/problems/missing-number/
"""
Python
----
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i, n in enumerate(nums):
            res += (i - n)
            
        return res
        
C++
----
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = nums.size();
        for (int i = 0; i < nums.size(); i++)
        {
            ans += (i - nums[i]);
        }
        return ans;
        
    }
};

