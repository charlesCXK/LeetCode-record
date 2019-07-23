# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def getReverse(head):
            if not head or not head.next:
                return head, head
            newhead, last = getReverse(head.next)
            last.next = head
            head.next = None

            return newhead, head
        
        newhead, last = getReverse(head)
        return newhead