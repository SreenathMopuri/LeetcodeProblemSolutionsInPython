# 15. 3Sum
"""
leetcode link: https://leetcode.com/problems/3sum/
"""
C++
---
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return {};
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n-2; ++i)
        {
            if (i == 0 || nums[i] != nums[i-1])
            {
                int j = i + 1, k = n - 1;
                while (j < k)
                {
                    int sum = nums[i] + nums[j] + nums[k];
                    if (sum == 0)
                    {
                        result.push_back({nums[i], nums[j], nums[k]});
                        while(j < k && nums[j] == nums[j+1]) j++;
                        while(j < k && nums[k] == nums[k-1]) k--;
                        j++, k--;
                    }
                    else if (sum > 0) k--;
                    else j++;             
                }
            }
        }
        return result;
    }
};


Python
------
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3: return []
        
        res = []
        nums.sort()
        
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, n-1
                while j < k:
                    sum1 = nums[i] + nums[j] + nums[k]
                    if sum1 == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]: j += 1
                        while j < k and nums[k] == nums[k-1]: k -= 1
                        j, k = j+1, k-1
                    elif sum1 < 0: j += 1
                    else: k -= 1
        return res
