class Codec:

    def serialize(self, root):
        if not root:
            return ""
        cur = [root]
        res = str(root.val)
        while cur:
            t = cur.pop(0)
            if t.left:
                cur.append(t.left)
                res += "," + str(t.left.val)
            else:
                res += ",x"
            if t.right:
                cur.append(t.right)
                res += "," + str(t.right.val)
            else:
                res += ",x"
        return res

    def deserialize(self, data):
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        cur = [root]
        i = 1
        while cur:
            t = cur.pop(0)

            # left child
            if data[i] != "x":
                t.left = TreeNode(int(data[i]))
                cur.append(t.left)
            i += 1

            # right child
            if data[i] != "x":
                t.right = TreeNode(int(data[i]))
                cur.append(t.right)
            i += 1

        return root