# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = [root]
        l = []
        while cur:
            t = cur.pop(0)
            l.append(t.val)
            if t.left:
                cur.append(t.left)
            if t.right:
                cur.append(t.right)
        l.sort()
        return l[k-1]