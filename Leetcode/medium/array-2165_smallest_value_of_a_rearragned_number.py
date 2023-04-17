class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """

        sorted_num = sorted(str(abs(num)))

        if num < 0:
            return -int(''.join(sorted_num[::-1]))
        
        
        for i in range(0,len(sorted_num)):
            if sorted_num[i] > '0':
                sorted_num[i], sorted_num[0] = sorted_num[0],sorted_num[i]
                break
    

        return int(''.join(sorted_num))



sol = Solution()
print(sol.smallestNumber(310))