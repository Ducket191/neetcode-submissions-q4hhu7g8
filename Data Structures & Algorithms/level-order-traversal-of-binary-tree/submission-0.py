# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = [root]
        res = []
        if not root: return res
        while cur:
            res2 = []
            c = []
            for item in cur:
                res2.append(item.val)
                if item.left:
                    c.append(item.left)
                if item.right:
                    c.append(item.right)
            cur = c
            res.append(res2)
        return res

