# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def dfs(lst):
            n = len(lst)
            if n == 0:
                return None
            mid = n // 2
            root = TreeNode(lst[mid])
            root.left = dfs(lst[:mid])
            root.right = dfs(lst[mid+1:])
            return root
            
        
        nodes = []
        it = head
        while it:
            nodes.append(it.val)
            it = it.next
        
        return dfs(nodes)
    