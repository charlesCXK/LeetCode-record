'''
Runtime: 48 ms, faster than 91.72% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = []
        q.append([root, 1])
        while len(q):
            top, step = q.pop(0)
            if not top.left and not top.right:
                return step
            if top.left:
                q.append([top.left, step+1])
            if top.right:
                q.append([top.right, step+1])
                