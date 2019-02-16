'''
48 ms
在递归函数参数中引入最大最小值。左侧子树不能大于当前节点的值，右侧子树不能小于当前节点的值
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, minV, maxV):
        if minV >= root.val or maxV <= root.val:
            return False
        
        leftV, rightV = True, True
        
        if root.left:
            leftV = self.dfs(root.left, minV, root.val)
        if root.right:
            rightV = self.dfs(root.right, root.val, maxV)
        
        return leftV and rightV
            
            
    def isValidBST(self, root: 'TreeNode') -> 'bool':        
        # empty node
        if not root:
            return True
        
        return self.dfs(root, -9999999999, 9999999999)