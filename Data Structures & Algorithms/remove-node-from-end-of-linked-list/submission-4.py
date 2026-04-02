# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev_head = self.reverse(head)
        prev = rev_head
        if n == 1:
            prev = prev.next
            res = self.reverse(prev)
            return res
        i = 1
        while i < n-1:
            prev = prev.next
            i += 1
        if prev.next and prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        res = self.reverse(rev_head)
        return res

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev