# 190. Reverse Bits
"""
leetcode link: https://leetcode.com/problems/reverse-bits/
"""

Python
------
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))
        return res
        
 C++
-----
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        
        for (int i=0; i < 32; i++)
        {
            int bit = (n >> i) & 1;
            res |= (bit << (31 - i));
        }
        return res;
        
    }
};
