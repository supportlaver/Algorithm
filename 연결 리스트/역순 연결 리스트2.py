# 인덱스 m 에서 n 까지를 역순으로 만들고, 인덱스 m 은 1부터 시작한다.
# input1 : 1 -> 2 -> 3 -> 4 -> 5 -> NULL , m = 2 , n = 4
# output1 : 1 -> 4 -> 3 -> 2 -> 5 -> NULL
from typing import ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        # 예외 처리
        if not head or m == n:
            return head
        
        # None 인 노드를 생성하고 head 앞에 생성해줌으로써 return root.next 를 하면 된다.
        root = start = ListNode(None)
        root.next = head

        for _ in range(left-1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        # 예시 input1 로 해보면 첫 번째 다중 할당으로 인해 1 -> 3 , 2 -> 4 를 가리키게 된다.
        # 여기서 3 와 2 를 이어주면 되는데 이것을 이어주기 위해서 tmp 라는 변수가 필요하다.
        # 해당 과정을 right-left 번 반복하면 역순으로 만들어진다.
        # 참고 : https://bellog.tistory.com/140
        for _ in range(right-left):
            tmp ,start.next , end.next = start.next , end.next , end.next.next
            start.next.next = tmp
        return root.next