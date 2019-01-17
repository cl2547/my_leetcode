class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.left!=None and root.right!=None:
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        elif root.left != None and root.right == None:
            root.right = root.left
            root.right = self.invertTree(root.right)
            root.left = None
        elif root.left == None and root.right != None:
            root.left = root.right
            root.left = self.invertTree(root.left)
            root.right = None
        else:
            return root
        return root