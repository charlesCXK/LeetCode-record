# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        myhead = ListNode(0)       # make a new head node
        myhead.next = head
        
        list_len = 0
        it = myhead
        while it.next:
            list_len += 1
            it = it.next
    
        it = myhead
        front = list_len - n
        while front:        # remove elements in the front
            it = it.next
            front -= 1
        if it.next:         # remove the selected element
            it.next = it.next.next
        return myhead.next
        
        
            