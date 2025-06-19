# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] == arr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        