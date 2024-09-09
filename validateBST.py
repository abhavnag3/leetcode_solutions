# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        ''' passes intial test cases  (53/85) then fails
        if not root:
            return
        if root.left and root.left.val < root.val:
            self.isValidBST(root.left)
            
        if root.right and root.right.val > root.val:
            self.isValidBST(root.right)
            return True
        else:
            return False
        '''
        
        
        def helprr(node, left, right):

            if node is None:
                return True
            if not (left < node.val < right):
                return False
            else:
                return helprr(node.left, left, node.val) and helprr(node.right, node.val, right)

        return helprr(root, float('-inf'), float('inf'))
        
        '''
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))
        '''