from typing import ListNode , List

# input1
# 2 -> 4 -> 3 + 5-> 6-> 4

# output1
# 7 -> 0 -> 8

# 342 + 465 = 807

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head:ListNode) -> ListNode:
    node , prev = head , None
    while node:
        next,node.next = node.next , prev
        prev , node = node , next
    return prev


# 파이썬 리스트를 연결 리스트로 변환
def toReversedLinkedList(result:str) -> ListNode:
    prev : ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
    return node

# 연결 리스트를 파이썬 리스트로 변환
def toList(node:ListNode) -> List:
    list: List = []
    while node:
        list.append(node.val)
        node = node.next
    return list


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    reverse_l1 = toList(reverseList(l1))
    reverse_l2 = toList(reverseList(l2))
    result_str = int(''.join(str(l1) for l1 in reverse_l1)) + int(''.join(str(l2) for l2 in reverse_l2))

    return toReversedLinkedList(result_str)




