# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        q = deque()
        q.append(root)
        while len(q)> 0:
            tmp = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    tmp.append(cur.left.val)
                    q.append(cur.left)
                if cur.right:
                    tmp.append(cur.right.val)
                    q.append(cur.right)
            if len(tmp) > 0:
                res.append(tmp)
        return res
            
