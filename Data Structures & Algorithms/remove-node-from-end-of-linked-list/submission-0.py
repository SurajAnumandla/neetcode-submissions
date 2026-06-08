# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head

        curr = head
        count = 0
        while curr!=None:
            curr=curr.next
            count+=1

        if count == n:
            head = head.next
            return head

        curr = head

        for i in range(count-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head