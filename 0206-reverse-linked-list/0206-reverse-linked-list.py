# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.reverse()

        rlist = ListNode()
        curr = rlist

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return rlist.next

        