# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        x = preorder.pop(0)
        root = TreeNode(x)
        y = inorder.index(x)
        l, r = inorder[:y], inorder[y+1:]
        if l:
            root.left = self.buildTree(preorder, l)
        if r:
            root.right = self.buildTree(preorder, r)
        return root