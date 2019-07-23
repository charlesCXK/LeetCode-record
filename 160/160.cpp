/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * Use two pointers, referring to the official solution
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *itA = headA;
        ListNode *itB = headB;
        int iterA = 0, iterB = 0;
        
        if(headA==NULL || headB==NULL)
            return NULL;
        
        while(itA != itB) {
            // reach the last of the node
            if(itA->next==NULL && itB->next==NULL) {
                if(itA->val == itB->val)
                    return itA;
                else
                    return NULL;
            }
            
            if(itA->next)
                itA = itA->next;
            else {
                if(iterA % 2 == 0)
                    itA = headB;
                else
                    itA = headA;
                iterA++;
            }

            if(itB->next)
                itB = itB->next;
            else {
                if(iterB % 2 == 0)
                    itB = headA;
                else
                    itB = headB;
                iterB++;
            }
        }  
        // itA and itB have met each other, this is the intersection node
        return itA;
    }
};