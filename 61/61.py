# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:  
        if not head:
            return None
        it = head
        end = it
        list_len = 1
        while it.next:
            list_len += 1
            it = it.next
            end = it
        
        if list_len == 1:
            return head
                    
        end.next = head     # connect begin and end
        move_num = list_len - (k%list_len)        # move k steps to the right, get the new head
        
        it, former = head, end
        while move_num:
            it = it.next
            former = former.next
            move_num -= 1
        former.next = None
        
        return it