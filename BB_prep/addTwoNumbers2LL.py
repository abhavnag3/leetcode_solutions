class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        revL1 = self.reverseLL(l1)
        revL2 = self.reverseLL(l2)
        
        print("L1: ", revL1)
        print("L2: ", revL2)
        
        added = self.addTwoLists(revL1, revL2)
        print("added: ", added)
        
        return self.reverseLL(added)
        
    def addTwoLists(self, l1, l2):
        
        l3 = ListNode(-1)
        prev = l3
        carry = 0
        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            curr_sum = l1_val + l2_val + carry
            
            carry = curr_sum // 10
            prev.next = ListNode(curr_sum % 10)
            prev=prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l3.next
            
    
    
    def reverseLL(self, head):
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev