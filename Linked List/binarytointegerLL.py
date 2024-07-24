# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        ###############################################
        #code
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum=0
        while head:
            sum=sum*2+head.val
            head=head.next
        return sum
    #################################################
# Create a linked list 1 -> 0 -> 1 which represents the binary number '101'
node3 = ListNode(1)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)

# Instantiate the Solution class
solution = Solution()

# Get the decimal value of the binary number
decimal_value = solution.getDecimalValue(node1)
print(decimal_value)  # Output: 5 (since 101 in binary is 5 in decimal)
