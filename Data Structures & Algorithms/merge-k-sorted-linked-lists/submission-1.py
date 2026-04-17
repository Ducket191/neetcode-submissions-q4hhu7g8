# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        x = self.merge2(lists[0], lists[1])
        for i in range(2, len(lists)):
            x = self.merge2(x, lists[i])
        return x

    def merge2(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = res = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                res = res.next
                list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next
        
        if list1:
            res.next = list1
        elif list2:
            res.next = list2
        
        return dummy.next
            
        
        