# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        '''
        three possible cases i think:
        (1) root is not none and subroot is not none
        (2) root is none and subroot is not none
        (3) both root and subroot is none 
        '''

        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        return False



        '''
        if root is None and subRoot is None:
            return True
        if root and subRoot:
            if root.val == subRoot.val:
                return self.isSubtree(root.right, subRoot.right) and self.isSubtree(root.left, subRoot.left)
            else:
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        else:
            return False
        '''
    