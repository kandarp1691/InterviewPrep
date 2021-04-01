import heapq
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        stack = []
        heap = []
        stack.append(root)
        while len(stack) is not 0:
            r = stack.pop(0)
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
            heapq.heappush(heap, r.val)
        return heap[k-1]

