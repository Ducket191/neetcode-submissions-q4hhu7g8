# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        cur = [root]
        curD = 1
        while cur:
            new = []
            for item in cur:
                if item.left:
                    new.append(item.left)
                if item.right:
                    new.append(item.right)
            cur = new
            if cur:
                curD += 1
        return curD