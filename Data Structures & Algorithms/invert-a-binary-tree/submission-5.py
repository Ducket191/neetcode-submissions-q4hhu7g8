class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        cur = [root]

        while cur:
            item = cur.pop(0)  # instead of remove() inside loop

            item.left, item.right = item.right, item.left

            if item.left:
                cur.append(item.left)
            if item.right:
                cur.append(item.right)

        return root