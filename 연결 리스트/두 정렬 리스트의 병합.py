# 입력 L1 : 1->2->4 , L2 : 1->3->4
# 출력 : 1->1->2->3->4->4
# 정렬되어 있는 두 리스트를 합치기

from typing import ListNode
def mergeTwoLists(l1:ListNode, l2:ListNode) -> ListNode:

    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2,l1
    if l1:
        l1.next = mergeTwoLists(l1.next,l2)
    return l1