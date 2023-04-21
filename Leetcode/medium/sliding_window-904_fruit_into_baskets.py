
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(fruits)):
            for j in range(1,len(fruits)):
                count = []
                for k in range(i,j+1):
                    if fruits[k] not in count:
                        count.append(fruits[k])
                if len(count) <= 2:
                    res = max(res,j+1-i)


        
        





fruits =[1,2]
sol = Solution()
sol.totalFruit(fruits)
