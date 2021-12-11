#4. Median of Two Sorted Arrays
"""
Leetcode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
Python
-----
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        # ensure that nums1's length become shorter by exchanging nums1 and nums2
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        start = 0
        end = n
        while start <= end:
            median1 = (start + end) // 2  # Median for first array
            median2 = (n + m + 1) // 2 - median1 # Median for second array
            left1 = -float('inf') if median1 == 0 else nums1[median1-1]
            right1 = float('inf') if median1 == n else nums1[median1]
            left2 = -float('inf') if median2 == 0 else nums2[median2-1]
            right2 = float('inf') if median2 == m else nums2[median2]
            if left1 <= right2 and left2 <= right1:
                if (n + m) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                end = median1-1
            else:
                start = median1+1
                
C++
----
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(); //size of first array
        int m=nums2.size(); // size of second array
        if(m < n) // if second array size is less than first array
           return findMedianSortedArrays(nums2,nums1);
            
        int low = 0, high = n; // first Array low and high variables
        while(low <= high) // low is less than are equal
        {
            int mid1 = (low + high) / 2; // middle of first array
            int mid2 = (n + m + 1) / 2 - mid1; // middle of second array
            int left1 = mid1 <= 0 ? INT_MIN : nums1[mid1-1];
            int left2 = mid2 <= 0 ? INT_MIN : nums2[mid2-1];
            int right1 = mid1 == n ? INT_MAX : nums1[mid1];
            int right2 = mid2 == m ? INT_MAX : nums2[mid2];
            if(left1 <= right2 && left2 <= right1)
            {
                if((n + m) % 2) //odd
                    return max(left1, left2);
                else                       //even
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
            }
            if(left1 > left2)
                high = mid1 - 1;
            else
                low = mid1 + 1;     
        }
        
        return 0.0;
    }
};
