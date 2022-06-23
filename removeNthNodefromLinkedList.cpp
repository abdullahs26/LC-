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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *p_temp = head;
        ListNode *p_temp2 = head;
        ListNode *p_temp3 = head;
        
        for (int i = 0; i < n; i++){
            p_temp = p_temp -> next;                   
        }
        
        if (p_temp == nullptr)
            return head->next;
        
      while (p_temp != nullptr){
          p_temp3 = p_temp2;
          p_temp2 = p_temp2 -> next;
          p_temp = p_temp -> next;
      }
        
       p_temp3 -> next = p_temp2 -> next;
       return head;
    }
    
};