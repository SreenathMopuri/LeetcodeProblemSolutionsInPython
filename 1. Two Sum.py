# Two Sum Problem
"""
use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice;
Leetcode link: https://leetcode.com/problems/two-sum/
"""
Python
----
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return {}
    
    C++
    ----
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i=0; i < nums.size(); i++)
        {
            if(map.count(target-nums[i])) return {map[target-nums[i]], i};
            map[nums[i]] = i;
        }
         return {};
    }
};
