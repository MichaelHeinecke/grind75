from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    def reverseListRecursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseListRecursively(head.next)
            head.next.next = head

        head.next = None
        return new_head
