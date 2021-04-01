# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        stack.append(root)
        stack.append(root)
        while len(stack) != 0:
            t1 = stack.pop(0)
            t2 = stack.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1.val != t2.val:
                return False
            if t1 is None or t2 is None:
                return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)
        return True
