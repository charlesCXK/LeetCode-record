# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
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
        
        '''
        reverse even rows
        '''
        for i in range(1, len(ret), 2):
            ret[i].reverse()
        
        return ret
        