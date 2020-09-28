# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        soln = ListNode()
        head = soln
        while l1 or l2:
            if not l1:
                digit = carry + l2.val
                l2 = l2.next
            elif not l2:
                digit = carry + l1.val
                l1 = l1.next
            else:
                digit = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            carry = 0
            if digit >= 10:
                digit = digit % 10
                carry = 1
            soln.val = digit
            if l1 or l2:
                soln.next = ListNode()
                soln = soln.next
        if carry:
            soln.next = ListNode()
            soln.next.val = carry
        return head