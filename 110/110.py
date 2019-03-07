'''
Runtime: 64 ms, faster than 75.01% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        def calculateHeight(root):
            if not root:
                return 0
            leftHeight = calculateHeight(root.left)
            rightHeight = calculateHeight(root.right)
            
            if abs(leftHeight-rightHeight) > 1:
                self.flag = False
                return 0
            return max(leftHeight, rightHeight) + 1
        
        calculateHeight(root)
        return self.flag