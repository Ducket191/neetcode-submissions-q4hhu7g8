# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = [root]
        res = root
        if not root:
            return root
        while cur:
            for item in cur:
                dummy = item.left
                item.left = item.right
                item.right = dummy
                cur.remove(item)
                if item.left:
                    cur.append(item.left)
                if item.right:
                    cur.append(item.right)
        return res