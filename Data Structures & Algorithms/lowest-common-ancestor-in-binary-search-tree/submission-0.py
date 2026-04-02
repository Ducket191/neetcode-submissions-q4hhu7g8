# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        target = [p.val, q.val]
        res = root
        cur = root
        while True:
            if cur.right and self.Search(cur.right, p.val) and self.Search(cur.right, q.val):
                cur = cur.right
                res = cur
            elif cur.left and self.Search(cur.left, p.val) and self.Search(cur.left, q.val):
                cur = cur.left
                res = cur
            else:
                break
        return res          

    def Search(self, root: TreeNode, target: int) -> bool:
        cur = [root]
        while cur:
            t = cur.pop(0)
            if t.val == target:
                return True
            if t.left:
                cur.append(t.left)
            if t.right:
                cur.append(t.right)
        return False
