'''
对称的必要条件：
1. 中序遍历得到的序列应该是左右对称的    (191/193 passed)
2. 中序遍历和逆中序遍历得到的序列应该是相同的    (192/193 passed)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    nodelist = []
    # 中序遍历
    # root.left, root, root.right
    def inorder(self, root):
        if not root:
            return
        
        isLeaf = False
        if not root.left and not root.right:
            isLeaf = True
        
        if root.left:
            self.inorder(root.left)
        elif not isLeaf:
            self.nodelist.append(None)
            
        self.nodelist.append(root.val)
        
        if root.right:
            self.inorder(root.right)
        elif not isLeaf:
            self.nodelist.append(None)

    # 逆中序遍历
    # root.right, root, root.left
    def reverseInorder(self, root):
        if not root:
            return
        
        isLeaf = False
        if not root.left and not root.right:
            isLeaf = True
        
        if root.right:
            self.reverseInorder(root.right)
        elif not isLeaf:
            self.nodelist.append(None)
            
        self.nodelist.append(root.val)
        
        if root.left:
            self.reverseInorder(root.left)
        elif not isLeaf:
            self.nodelist.append(None)
            
    
    def judge(self, lst1, lst2):
        len1, len2 = len(lst1), len(lst2)
        if len1 != len2:
            return False
        for i in range(len1):
            if lst1[i] != lst2[i]:
                return False
        return True

        
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        self.nodelist = []
        self.inorder(root)
        lst1 = self.nodelist.copy()
        # print(self.nodelist)
        
        self.nodelist = []
        self.reverseInorder(root)
        lst2 = self.nodelist.copy()
        # print(self.nodelist)
        
        if self.judge(lst1, lst2):
            # special judgement
            if root and root.left and root.right:
                if root.left.val != root.right.val:
                    return False
            return True
        return False