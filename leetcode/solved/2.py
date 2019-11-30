# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num, depth = 0, 0

        curr_node = l1
        while curr_node is not None:
            num += curr_node.val * (10 ** depth)
            depth += 1
            curr_node = curr_node.next
            
        depth = 0
        curr_node = l2
        while curr_node is not None:
            num += curr_node.val * (10 ** depth)
            depth += 1
            curr_node = curr_node.next
            
        result = ListNode(num % 10)
        num = num // 10
        curr_node = result
        while num > 0:
            curr_node.next = ListNode(num % 10)
            curr_node = curr_node.next
            num = num // 10
        
        return result
            