# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        while head:
            head.next = self.reverse(head.next)
            head = head.next

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev
        