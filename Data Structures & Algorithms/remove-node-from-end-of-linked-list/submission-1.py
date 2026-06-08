# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Approach 1 -> find the size and delete

        # if head.next is None:
        #     head = None
        #     return head

        # curr = head
        # count = 0
        # while curr!=None:
        #     curr=curr.next
        #     count+=1

        # if count == n:
        #     head = head.next
        #     return head

        # curr = head

        # for i in range(count-n-1):
        #     curr = curr.next
        # curr.next = curr.next.next
        # return head


        #Approach 2 -> slow and fast pointer
        if head is None or head.next is None:
            return None

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            head = head.next
            return head

        while fast.next!=None:
            slow = slow.next
            fast=fast.next
        slow.next = slow.next.next
        return head
