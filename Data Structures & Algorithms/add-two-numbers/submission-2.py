# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        first = dummy
        carry = 0
        while l1 or l2:
            _sum = carry
            carry = 0
            if l1:
                _sum+=l1.val
                l1=l1.next
            if l2:
                _sum+=l2.val
                l2=l2.next
            if _sum >9:
                carry = 1
                _sum = _sum%10
            node = ListNode(_sum)
            first.next = node
            first = first.next
        if carry>0:
            node = ListNode(carry)
            first.next = node
        return dummy.next