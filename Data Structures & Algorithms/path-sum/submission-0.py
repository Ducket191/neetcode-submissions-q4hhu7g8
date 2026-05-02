# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, s):
            if not root:
                return False
            s.append(root.val)
            if sum(s) == targetSum and not root.left and not root.right:
                return True
            if dfs(root.left, s):
                return True
            if dfs(root.right, s):
                return True
            s.pop()            

            return False
        return dfs(root, [])