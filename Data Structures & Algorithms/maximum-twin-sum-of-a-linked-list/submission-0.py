# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        m = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur, prev = slow, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        while prev:
            m = max(prev.val + head.val, m)
            prev = prev.next
            head = head.next
        return m