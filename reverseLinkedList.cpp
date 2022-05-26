/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
     ListNode* reverseList(ListNode* head) {
        if(head == nullptr || head->next == nullptr) 
            return head;
         
		ListNode* p = nullptr;
        ListNode* c = head;
         
        while (c -> next != NULL) {
            ListNode *temp = c;
            c = c -> next;
            temp -> next = p;
            p = temp;
        }
         
         c -> next = p;
		
        return c;
    }
};