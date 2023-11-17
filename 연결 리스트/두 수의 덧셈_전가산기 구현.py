from typing import ListNode

# 2 -> 4 -> 3 + 5 -> 6 -> 4
# 7 -> 0 -> 8


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0

    while l1 or l2 or carry:
        sum = 0

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        carry , val = divmod(sum + carry , 10)
        head.next = ListNode(val)
        head = head.next
    return root.next