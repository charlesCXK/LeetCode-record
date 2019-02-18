'''
Runtime: 44 ms, faster than 99.96% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1