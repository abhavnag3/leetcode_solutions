# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
        '''# 6 + 4 = 10, 0 
        p = l1
        q = l2
        sum_tot = []
        carry_over = 0
        while p is not None and q is not None:
            curr_sum = carry_over + p.val + q.val
            carry_over = int(curr_sum / 10)
            sum_tot.append(curr_sum % 10)
            p = p.next
            q = q.next
        
        #9,9,9,9,9
        #      9,9
        #       1  8
        print(sum_tot)
        if q is None:
            # do stuff for leftover of p
            while p is not None:
                curr_sum = carry_over + p.val
                carry_over = int(curr_sum / 10)
                sum_tot.append(curr_sum % 10)
                p = p.next
        elif p is None:
            # do stuff for leftover of q
            while q is not None:
                curr_sum = carry_over + p.val
                carry_over = int(curr_sum / 10)
                sum_tot.append(curr_sum % 10)
                q = q.next
        if carry_over != 0:
            sum_tot.append(carry_over)
        newNode = ListNode(-1)
        p = newNode
        for i in range(1, len(sum_tot)):
            ln = ListNode(sum_tot[i], None)
            newNode.next = ln
            newNode = newNode.next
        print(newNode.val)
        print(sum_tot)
        return newNode.next'''
        
#9,9,9,9
#    9,9
#10 0 9 8
            
            