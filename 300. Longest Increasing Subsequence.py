# 300. Longest Increasing Subsequence
"""
Leetcode link: https://leetcode.com/problems/longest-increasing-subsequence/
Solution:
recursive: foreach num, get subseq with num and without num, only include num if prev was less, cache solution of each; 
dp=subseq length which must end with each num, curr num must be after a prev dp or by itself;
"""
Python
------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j]+1)
        return max(LIS)
 
C++
----
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = nums.size();
        vector<int> v1(size, 1);
        
        for (int i = size-1; i>=0; i--)
        {
            for (int j = i+1; j < size; j++)
            {
                if (nums[i] < nums[j])
                    v1[i] = max(v1[i], 1 + v1[j]);
            }
        }
        return *max_element(v1.begin(), v1.end());
        
    }
};
