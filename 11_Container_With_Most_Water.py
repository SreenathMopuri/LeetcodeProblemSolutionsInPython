# 11. Container With Most Water
"""
leetcode link: https://leetcode.com/problems/container-with-most-water/
Shrinking window, left/right initially at endpoints, shift the pointer with min height
"""

Python
------
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
        
        
C++
----
class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        int left = 0, right = height.size() - 1;
        
        while (left < right)
        {
            int area = (right -left) * min(height[left], height[right]);
            result = max(result, area);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return result;
        
    }
};
