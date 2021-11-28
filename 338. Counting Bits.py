# 338. Counting Bits
"""
leetcode link: https://leetcode.com/problems/counting-bits/
"""

C++
----
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1);
        int offset = 1;
        
        for (int i=1; i<n+1; i++)
        {
            if (offset * 2 == i)
                offset = i;
            dp[i] = 1 + dp[i - offset];
        }
        return dp;
        
    }
};


Python
-----
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]* (n+1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
            
"""
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
""""
