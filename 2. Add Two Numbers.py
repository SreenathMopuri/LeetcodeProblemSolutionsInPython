#2. Add Two Numbers
"""
Leetcode link: https://leetcode.com/problems/add-two-numbers/
"""
Python
-----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur =ListNode(0)
        
        carry = 0
        
        while(l1 or l2 or carry):
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //=10
        return dummy.next
        
   C++
  ----
  class Solution {
public:
    ListNode* addTwoNumbers(ListNode* List1, ListNode* List2) {
         ListNode head(0);
        ListNode* curr = &head;
        
        int carry = 0;
        
        while (List1 || List2 || carry)
        {
            int x = List1 ? List1->val : 0;
            int y = List2 ? List2->val : 0;
            
            ListNode* node = new ListNode((x + y + carry) % 10);
            curr->next = node;
            curr = node;
            carry = (x + y + carry) / 10;
            
            if(List1) List1 = List1->next;
            if(List2) List2 = List2->next;
        }
        return head.next;
    }
};
