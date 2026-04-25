# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def inorder(root: Optional[TreeNode], arr: List[int]) -> List[int]:
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
            return arr
        return inorder(root, [])