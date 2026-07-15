# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        mid = slow
        rev = slow

        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp

        curr = head
        res = head
        while curr!=mid:
            if not prev.next:
                break
            temp = curr.next
            opp = prev.next
            curr.next = prev
            prev.next = temp
            prev = opp
            curr = temp
        head = res
