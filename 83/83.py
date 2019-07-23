# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        it = head
        if not it:
            return None
        while it.next:
            if it.next.val == it.val:
                it.next = it.next.next
            else:
                it = it.next
        return head
            
        