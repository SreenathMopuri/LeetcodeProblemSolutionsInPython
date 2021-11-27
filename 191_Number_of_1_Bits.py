# 191. Number of 1 Bits
"""
https://leetcode.com/problems/number-of-1-bits/
"""

C++
----
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while (n)
        {
            n = n & (n -1);
            res += 1;
        }
        return res;
    }
};

Python
------
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        
