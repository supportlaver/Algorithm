from typing import ListNode
# input : 1 -> 2 -> 3 -> 4
# output : 2 -> 1 -> 4 -> 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 값만 변경하는 기본적인 방법
def pairSwap_basic(head: ListNode) -> ListNode:
    
    node = head

    while node and node.next:
        node.val , node.next.val = node.next.val = node.val
        node = node.next.next

# 반복 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head
        prev.next = b

        prev = prev.next.next
        head = head.next
    return root.next
                