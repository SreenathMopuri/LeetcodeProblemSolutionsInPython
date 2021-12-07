# 70. Climbing Stairs
"""
leetcode link: https://leetcode.com/problems/climbing-stairs/
"""
Python
-----
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one
       
 C++
---
class Solution {
public:
    int climbStairs(int n) {
        int one = 1, two = 1;
        
        for (int i = 0; i < n -1; i++)
        {
            int temp = one;
            one = one + two;
            two = temp;
        }
        return one;
        
    }
};
