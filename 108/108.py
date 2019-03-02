'''
Runtime: 84 ms, faster than 34.73% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        n = len(nums)
        if n == 0:
            return None
        
        center = n//2
        root = TreeNode(nums[center])
        root.left = self.sortedArrayToBST(nums[:center])
        root.right = self.sortedArrayToBST(nums[center+1:])
        
        return root
        