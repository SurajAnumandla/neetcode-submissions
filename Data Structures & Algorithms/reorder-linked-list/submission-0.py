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
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        if fast is None:
            fast = prev
        curr = head
        while curr!= slow:
            if fast.next is None:
                break
            temp_l = curr.next
            temp_r = fast.next
            curr.next = fast
            fast.next = temp_l
            curr =temp_l
            fast = temp_r

        return