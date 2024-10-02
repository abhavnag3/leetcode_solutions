class Solution

	def reverseLinkedList(head, left, right):
		dummyNode = ListNode(0, head)

		prevLeft = dummyNode
		curr = head
		for i in range(left - 1):
			prev, curr = curr, curr.next
		
		#(2) reverse the list from left all the way to rigt
		
		prev = None
		for i in range(right - left + 1):
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		
		#(3) swap the pointer from right before the sub list and right after
		prevLeft.next.next = curr
		prevLeft.next = prev #becaues remember even from the RLL1 that prev is the beginning of the reversed linked list
		
		return dummyNode.next
