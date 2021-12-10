# 1143. Longest Common Subsequence
"""
Leetcode link: https://leetcode.com/problems/longest-common-subsequence/
Solution:
recursive: if first chars are equal find lcs of remaining of each, else max of: lcs of first and remain of
2nd and lcs of 2nd remain of first, cache result; nested forloop to compute the cache without recursion;
"""
Python
----
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1)+1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j]= max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        

C++
---
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>>dp(text1.length()+1, vector<int>(text2.length()+1, 0));
        
        for(int i = text1.length()-1; i>=0; i--)
            for (int j = text2.length()-1; j >=0; j--)
            {
                if (text1[i] == text2[j])
                    dp[i][j] = 1 + dp[i+1][j+1];
                else
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]);
            }
        return dp[0][0];
        
    }
};
