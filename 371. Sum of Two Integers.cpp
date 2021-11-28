# 371. Sum of Two Integers
"""
  leetcode link: https://leetcode.com/problems/sum-of-two-integers/
"""
 
  C++
  ---
  class Solution {
public:
    int getSum(int a, int b) {
        if ( 0 == a ) return b;
        if ( 0 == b ) return a;
        
        while ( b != 0 )
        {
            unsigned carry = a & b;
            a = a ^ b;
            b = carry << 1;            
        }
        return a;
    }
};
