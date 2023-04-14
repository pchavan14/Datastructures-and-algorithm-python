class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0

        while l1 is not None or l2 is not None:
            val1 = l1.val
            val2 = l2.val

            sum = ((val1 + val2) % 10 + carry)
            carry = (val1 + val2) // 10
            newnode = ListNode(sum)

            l1 = l1.next
            l2 = l2.next
        
    
            
            




list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)


list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

sol = Solution()
sol.addTwoNumbers(list1,list2)