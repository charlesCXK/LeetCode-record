# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.father = {}
        self.father[root] = None
        def mark(root):
            if not root:
                return
            if root.left:
                self.father[root.left] = root
                mark(root.left)
            if root.right:
                self.father[root.right] = root
                mark(root.right)
        
        mark(root)      # 获得每个节点的父节点
        father_p, father_q = [], []
        it = p
        while it:
            father_p.append(it)
            it = self.father[it]
        it = q
        while it:
            father_q.append(it)
            it = self.father[it]
        
        father_p = father_p[::-1]
        father_q = father_q[::-1]
        
        ret = None
        
        for i in range(min(len(father_p), len(father_q))):
            if father_p[i] == father_q[i]:
                ret = father_p[i]
            else:
                break

        return ret