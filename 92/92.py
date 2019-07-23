# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 让 [m, n] 区间内的 node，后一个指向前一个

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        myhead = ListNode(-1)
        myhead.next = head
        
        left = myhead   # get the (m-1)-th node
        for i in range(m-1):
            left = left.next
        
        it = left.next      # the m-th node
        it_next = it.next
        for i in range(n-m):
            the_third_node = it_next.next       # left -> m -> m+1 -> m+2
            it_next.next = it                   # left -> m <- m+1 -> m+2
            
            it = it_next                        # x <- it -> it_next
            it_next = the_third_node
        
        left.next.next = it_next
        left.next = it
        
        return myhead.next