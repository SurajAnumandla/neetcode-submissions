# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        k = 0

        while slow:
            slow=slow.next
            k+=1
        if k==n:
            return head.next
        slow = head
        for i in range(k-n-1):
            slow = slow.next
        slow.next = slow.next.next
        return head