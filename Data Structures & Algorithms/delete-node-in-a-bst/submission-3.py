# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                minval = self.minValue(root.right)
                root.val = minval
                root.right = self.deleteNode(root.right, minval)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
        return root

    def minValue(self, root: Optional[TreeNode]) -> int:
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur.val