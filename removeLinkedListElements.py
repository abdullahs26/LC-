# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        # Create dummy node
        temp = ListNode(0)
        temp.next = head
        iter = temp

        while iter.next:
            # find value in linked list, remove node by making next pointer point to next.next
            if iter.next.val == val:
                iter.next = iter.next.next
            else:
                iter = iter.next

        return temp.next