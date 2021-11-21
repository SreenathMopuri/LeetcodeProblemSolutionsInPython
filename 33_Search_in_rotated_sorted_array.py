# Search in rotated sorted array
"""
at most two sorted halfs, mid will be apart of left sorted or right sorted, if target is in range of sorted portion then search it, otherwise search other half
leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
C++
---
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        
        while (l <= r)
        {
            int mid = l + (r - l) / 2;
            if (target == nums[mid])
                return mid;
            
            // left sorted portion
            if (nums[l] <= nums[mid])
                if (target > nums[mid] || target < nums[l])
                    l = mid + 1;
                else
                    r = mid - 1;
            // right sorted portion
            else
                if (target < nums[mid] || target > nums[r])
                    r = mid - 1;
                else
                    l = mid + 1;
        }
        return -1;
    }
};

Python
-----
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
      
