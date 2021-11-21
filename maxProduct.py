# Maximum Product Subarray
"""
dp: compute max and max-abs-val for each prefix subarr;
leetcode link: https://leetcode.com/problems/maximum-product-subarray/
"""
C++
----
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int currMax = nums[0];
        int currMin = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            int tmp = currMax;
            currMax = max({nums[i], nums[i]*currMax, nums[i]*currMin});
            currMin = min({nums[i], nums[i] * tmp, nums[i]*currMin});
            res = max(res, currMax);
        }
        return res;
        
    }
};

Python:
--------
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        
        for i in range(1, len(nums)):
            tmp = currMax
            currMax = max(nums[i], currMax * nums[i], currMin * nums[i]);
            currMin = min(nums[i], tmp * nums[i], currMin * nums[i]);
            res = max(res, currMax)
        return res
        
