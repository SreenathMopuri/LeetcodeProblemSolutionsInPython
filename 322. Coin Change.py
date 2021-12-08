# 322. Coin Change
"""
Leetcode link: https://leetcode.com/problems/coin-change/
Solution:top-down approach 
Recursive dfs, for amount, branch for each coin, cache to store prev
coin_count for each amount; bottom-up: compute coins for amount = 1, up until n, 
using for each coin (amount - coin), cache prev values.
"""
Python:
 -----
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]* (amount+1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c]);
        return dp[amount] if dp[amount] != amount + 1 else -1
      
C++
----
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector <int> dp(amount+1, amount+1);
        
        dp[0] = 0;
        
        for (int a = 1; a < amount+1; a++)
        {
            for(int c = 0; c < coins.size(); c++)
            {
                if ((a - coins[c]) >= 0)
                    dp[a] = min(dp[a], 1 + dp[a-coins[c]]);
            }
        }
        if (dp[amount] != amount+1)
            return dp[amount];
        else
            return -1;
        
    }
};
