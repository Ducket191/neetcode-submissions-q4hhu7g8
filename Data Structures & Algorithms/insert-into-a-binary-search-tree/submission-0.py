# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = dummy = root
        if not root:
            return TreeNode(val)
        while root:
            if val > root.val:
                dummy = root
                root = root.right
            elif val < root.val:
                dummy = root
                root = root.left
        if val > dummy.val:
            dummy.right = TreeNode(val)
        else:
            dummy.left = TreeNode(val)
        return res