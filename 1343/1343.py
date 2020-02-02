# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sumDict = {}
        
        def calSum(root):
            if not root:
                return 0
            if not root.left and not root.right:
                sumDict[root] = root.val
                return root.val
            else:
                tmp = calSum(root.left) + calSum(root.right) + root.val
                sumDict[root] = tmp
                return tmp            
        
        treeSum = calSum(root)
        maxProduct = 0
        for k,v in sumDict.items():
            maxProduct = max(maxProduct, v*(treeSum-v))
        maxProduct %= (10**9+7)
        return maxProduct
        