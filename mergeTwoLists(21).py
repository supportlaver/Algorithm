from typing import List , Optional
import collections
import sys

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 반복
        dummy = ListNode(None)
        node = dummy
        
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        
        node.next = list1 or list2

        return dummy.next
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 재귀
        
        if not (list1 and list2):
            return list1 or list2
        
        if list1.val > list2.val:
            list2.next = self.mergeTwoLists2(list1 , list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists2(list1.next , list2)
            return list1
        



if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode()
    l2 = ListNode()
    l3 = ListNode()
    l4 = ListNode()
    l1.val = 1
    l1.next=l2

    l2.val = 2
    l2.next=l3

    l3.val = 2
    l3.next = l4

    l4.val = 1
    l4.next = None


    print(sol.isPalindrome(l1))


    


        
            
                





        
        

        
        
        
        
            
        