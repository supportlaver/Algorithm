from typing import ListNode

# input1
# 1 -> 2 -> 3 -> 4 -> 5 -> NULL

# output1
# 1 -> 3 -> 5 -> 2 -> 4-> NULL
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList_my_challenge(self, head:ListNode) -> ListNode:
        odd_list = ListNode(None)
        odd_head = head

        even_list = ListNode(None)
        even_head = head.next

        while odd_head is not None:
            odd_list.next = odd_head
            odd_head = odd_head.next

        while even_head is not None:
            even_list.next = even_head
            even_head = even_head.next
            
    def oddEvenList(self , head:ListNode) -> ListNode:

        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next , even.next = odd.next.next , even.next,next
            odd , even = odd.next , even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head

        
        


        