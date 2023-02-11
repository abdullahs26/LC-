# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Store head of linkedlist, use curr to iterate
        carry = 0
        temp = ListNode()
        curr = temp

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            newVal = value1 + value2 + carry
            # Floor division to calculate carry
            carry = newVal // 10
            # Use mod to get ones place value
            newVal = newVal % 10
            curr.next = ListNode(newVal)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next


        


        