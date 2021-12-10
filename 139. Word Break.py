#139. Word Break
"""
Leetcode link: https://leetcode.com/problems/word-break/
Solution:
for each prefix, if prefix is in dict and wordbreak(remaining str)=True, then 
return True, cache result of wordbreak;
"""
Python
------
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i+len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
                    
C++
---
class Solution {
public:
    int memo[301];//array as max limit length of string
    bool find(string s, int start, vector<string>& wordDict){
        if(start == s.length()) return true;
        if(memo[start] != -1) return memo[start];//checking if we have found result before
        
        bool res = false;
        for(int i = 0;i<wordDict.size();i++){
            if(s[start] != wordDict[i][0]) continue;//before checking whole word, just checking first char is macthing or not
            if(s.substr(start,wordDict[i].length()) == wordDict[i]){
                res = find(s,start+wordDict[i].length(),wordDict);
            }
            if(res) return memo[start] = true;//storing result in array
        }
        
        return memo[start] = false;//storing result in array
    }
    
    bool wordBreak(string s, vector<string>& wordDict) {
        memset(memo,-1,sizeof(memo));
        return find(s,0,wordDict); 
    }
};
