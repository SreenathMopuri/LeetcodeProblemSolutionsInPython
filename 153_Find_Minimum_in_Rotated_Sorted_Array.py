# Find Minimum in Rotated Sorted Array
"""
check if half of array is sorted in order to find pivot, arr is guaranteed to be in at most two sorted subarrays
leetcode link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Python
------
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
        
C++
----
class Solution {
public:
    int findMin(vector<int>& nums) {
        int res = nums[0];
        int l = 0, r = nums.size() - 1;
        while (l <= r)
        {
            if (nums[l] < nums[r])
            {
                res = min(res, nums[l]);
                break;
            }
            int m = l + (r -l) / 2;
            res = min(res, nums[m]);
            if (nums[m] >= nums[l])
                l = m + 1;
            else
                r = m - 1;
        }
        return res;
    }
};
