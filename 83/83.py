# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        res = []
        it = head
        
        # handle the first element
        # judge if it is an empty list
        if it:
            res.append(it.val)
            last = it
            it = it.next
        
        while it:
            if it.val != last.val:
                res.append(it.val)
            it = it.next
            last = last.next
        return res
            
        