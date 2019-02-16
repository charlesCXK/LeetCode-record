'''
对于一个节点的列表(单调的)，以其中某个节点为根节点，然后将列表分割成左右两部分，
左、右半部分分别递归构造节点树，作为根节点的左右子节点。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructTree(self, lst):
        if len(lst) == 0:
            return []
        
        nodelist = []
        for i in range(len(lst)):
            lefts = self.constructTree(lst[:i])
            rights = self.constructTree(lst[i+1:])
            for leftson in lefts or [None]:
                for rightson in rights or [None]:
                    root = TreeNode(lst[i])     # mark this node as root
                    root.left = leftson
                    root.right = rightson
                    nodelist.append(root)
        return nodelist
    
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        lst = range(1, n+1)
        nodeList = self.constructTree(lst)
        
        return nodeList
        