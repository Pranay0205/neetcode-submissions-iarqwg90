# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNum = ""
        while(l1 != None):
            firstNum += str(l1.val)
            l1 = l1.next

        secondNum = ""
        while(l2 != None):
            secondNum += str(l2.val)
            l2 = l2.next
        
        total = int(firstNum[::-1]) + int(secondNum[::-1])

        totalStr = str(total)[::-1]

        dummy = ListNode(0)
        curr = dummy
        for t in totalStr:
            curr.next = ListNode(int(t))
            curr = curr.next
        
        return dummy.next

            


        