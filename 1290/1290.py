# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        elements = []
        ret = 0
        
        while head:
            elements.append(head.val)
            head = head.next
        
        l = len(elements)
        base = 1
        
        for i in range(l):
            ret += elements[l-1-i] * base
            base *= 2
        return ret