# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cur1 = [p]
        cur2 = [q]
        while cur1 and cur2:
            t1 = cur1.pop(0)
            t2 = cur2.pop(0)
            if not t1 and not t2:
                continue
            elif not t1 and t2:
                return False
            elif t1 and not t2:
                return False
            elif t1 and t2:
                if t1.val != t2.val:
                    return False
                cur1.append(t1.left)
                cur1.append(t1.right)
                cur2.append(t2.left)
                cur2.append(t2.right)
        return True
