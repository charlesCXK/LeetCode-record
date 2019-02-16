'''
Runtime: 116 ms, faster than 74.97% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    nodelist = []
    wrong_num = []
    
    '''
    inorder traversal
    '''
    def inorder(self, root):
        if not root:
            return
        
        if root.left:
            self.inorder(root.left)
        self.nodelist.append(root.val)
        if root.right:
            self.inorder(root.right)
    
    '''
    traversal the tree, swap the number
    '''
    def travel(self, root, num1, num2):
        if not root:
            return
        if root.val == num1:
            root.val = num2
        elif root.val == num2:
            root.val = num1
        if root.left:
            self.travel(root.left, num1, num2)
        if root.right:
            self.travel(root.right, num1, num2)
        
    def recoverTree(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodelist = []
        self.wrong_num = []
        # inorder travel, getting the number list.
        # If it is a BST, the number list should be incremental
        self.inorder(root)
        
        # find the wrong 2 numbers
        self.nodelist = [-9999999999] + self.nodelist + [9999999999]
        
        for i in range(len(self.nodelist)-1):
            if self.nodelist[i] > self.nodelist[i+1]:
                self.wrong_num.append(self.nodelist[i])
                index1 = i
                break
        # find the other number
        if len(self.wrong_num) > 0:
            for i in range(index1+1, len(self.nodelist)-1):
                if self.nodelist[i]<self.wrong_num[0] and self.nodelist[i+1]>self.wrong_num[0]:
                    self.wrong_num.append(self.nodelist[i])
                    break
        
        # print(self.nodelist)
        # print(self.wrong_num)
        if len(self.wrong_num) > 0:
            self.travel(root, self.wrong_num[0], self.wrong_num[1])
        
        