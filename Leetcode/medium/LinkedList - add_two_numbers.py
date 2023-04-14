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
        #add the two numbers
        carry = 0
        dummy_head = ListNode(0)
        curr = dummy_head
        # 2 - > 4 - > 3
        # 5 - > 6 - > 4
        #7 - > 0 - > 8
        while l1 is not None or l2 is not None or carry !=0 :
            #digits which are overflowed
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0

            #digits which are overflowed
            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0

            sum = val1 + val2 + carry

            carry = (val1 + val2) // 10

            node = ListNode((val1 + val2)%10)

            curr.next = node
            curr = node

            #digits which are overflowed
            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

    
        return dummy_head.next


        
        
    
            
            




list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)


list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

sol = Solution()
sol.addTwoNumbers(list1,list2)