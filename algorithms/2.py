# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def add(self, l1=None, l2=None, carry=0):
        if l1 is None and l2 is None:
            return ListNode(1) if carry==1 else None
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0
        val = v1+v2+carry
        carry=0
        if(val>=10):
            val-=10
            carry=1
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
        return ListNode(val, self.add(l1,l2,carry))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1,l2,0)