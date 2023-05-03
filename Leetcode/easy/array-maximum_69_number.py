class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        list_num = list(str(num))
        
        for i in range(0,len(list_num)):
            if list_num[i] == '6':
                list_num[i] = '9'
                break
        

        return int(''.join(list_num))
       



num = 9999
sol = Solution()
print(sol.maximum69Number(num))