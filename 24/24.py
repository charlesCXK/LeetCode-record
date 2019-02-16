# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        left = head
        right = head.next
        
        # swap the first two nodes
        left.next = right.next
        right.next = left
        head = right
        left_former = left      # left_former: the node before left after entering the next loop
        
        while left.next:
            left = left.next
            if left.next:
                right = left.next
                # swap left and right
                left.next = right.next
                right.next = left
                left_former.next = right
            else:       # only one node left
                continue
            
            # At this time, 'left' is on the right and 'right' is on the left.
            left_former = left

        
        return head
        