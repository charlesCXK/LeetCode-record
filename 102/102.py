'''
Use a queue to get the level traversal of a tree.
Runtime: 40 ms, faster than 98.11% of Python3 online submissions 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        # empty node
        if not root:
            return []
        
        myqueue, ret = [], []
        myqueue.append([root, 1])       # push the first node into the queue
        
        while len(myqueue) > 0:
            thisnode = myqueue.pop(0)       # the front of the queue
            node, level = thisnode[0:2]
            if node.left:
                myqueue.append([node.left, level+1])
            if node.right:
                myqueue.append([node.right, level+1])
            if level > len(ret):
                ret.append([])
            ret[level-1].append(node.val)
        
        return ret
                
        