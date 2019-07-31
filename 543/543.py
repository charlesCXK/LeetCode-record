# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longest = 0
        
        def travel(root):
            if not root:
                return 0
            
            left_len, right_len = 0, 0
            if root.left:
                left_len = travel(root.left) + 1
            if root.right:
                right_len = travel(root.right) + 1
            if (left_len + right_len) > self.longest:
                self.longest = left_len + right_len
            return max(left_len, right_len)
        
        travel(root)
        return self.longest