# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        it = head
        while it:
            n += 1
            it = it.next
        
        # calculate the middle element's index
        mid = n//2
        
        # find the middle element
        n = 0
        it = head
        
        while n < mid:
            n += 1
            it = it.next
        return it