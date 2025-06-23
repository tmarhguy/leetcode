# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum, l2_sum, i = 0, 0, 0

        while l1 or l2:
            if l1:
                l1_sum += l1.val * 10 ** i
                l1 = l1.next
            if l2:
                l2_sum += l2.val * 10 ** i
                l2 = l2.next
            i += 1

        answers = [int(value) for value in str(l1_sum + l2_sum)]
        answers.reverse()

        dummy = ListNode()
        current = dummy

        for num in answers:
            current.next = ListNode(num)
            current = current.next
        return dummy.next