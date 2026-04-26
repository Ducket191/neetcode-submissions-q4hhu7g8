# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalance = True
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal isBalance
            if not root:
                return 0
            x = dfs(root.left)
            y = dfs(root.right)
            if abs(x-y) > 1:
                isBalance = False
            return max(x,y) + 1
        dfs(root)
        return isBalance