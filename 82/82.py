'''
[description]
两个指针遍历
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        it = head
        res = []
        
        while it:
            tmp = it.next
            if not tmp:
                res.append(it.val)
                break
                
            if tmp.val == it.val:
                while tmp and tmp.val == it.val:
                    tmp = tmp.next
                    it = it.next
                it = tmp
            else:
                res.append(it.val)
                it = it.next
        
        return res