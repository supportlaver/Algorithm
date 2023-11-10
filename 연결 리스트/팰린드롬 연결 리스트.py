# input : 1->2
# output : false

# input : 1->2->2->1
# output : true

from typing import ListNode , List
from collections import deque
# ListNode 를 파이썬의 List 로 변경한 후 팰린드롬 여부를 판단
def isPalindrome_1(head:ListNode)->bool:
    q : List = []

    if not head:
        return True
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

def isPalindrome_2(head:ListNode)->bool:
    q : deque = []

    if not head:
        return True
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True

# 런너 기법 사용
def isPalindrome_3(head:ListNode)->bool:
    rev = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev , rev.next , slow = slow , rev , slow.next
    
    # 홀수 일 때는 slow 런너가 한 칸 더 앞으로 이동하여 중앙의 값을 빗겨 나가야 함
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow,rev = slow.next , rev.next

    return not rev


    

