# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret = []
        if not root:
            return ret
        
        it = root
        while it or len(stack)>0:
            while it:
                stack.append(it)
                it = it.left
            
            last = stack.pop(-1)
            ret.append(last.val)
            it = last.right
        
        return ret
            