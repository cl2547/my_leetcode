# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1 #number of nodes
        
        def findLength(node):
            if not node: return 0
            left = findLength(node.left)
            right = findLength(node.right)
            #update max number of nodes found so far
            self.ans = max(self.ans, left+right+1)
            #retur the depth of a node
            return max(left,right)+1
        
        findLength(root)
        return self.ans-1