# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        y = l2
        x_sum = 0
        y_sum = 0
        i = 0

        while x or y:
            if x:
                x_sum += x.val * 10 ** i
                x = x.next
            if y:
                y_sum += y.val * 10 ** i
                y = y.next
            i += 1
        
        answer = [int(value) for value in str(x_sum+y_sum)]
        answer.reverse()
        
        dummy = ListNode()
        current = dummy

        for num in answer:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

        