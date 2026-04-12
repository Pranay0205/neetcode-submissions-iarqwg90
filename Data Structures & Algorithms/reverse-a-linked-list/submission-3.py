# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        res = []
        while curr != None:
            res.append(curr.val)
            curr = curr.next  

        dummy = ListNode()
        temp = dummy
        for i in range(len(res) - 1, -1, -1):
            temp.next = ListNode(res[i])
            temp = temp.next
        
        return dummy.next
            
        