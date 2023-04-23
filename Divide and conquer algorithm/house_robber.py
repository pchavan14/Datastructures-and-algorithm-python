class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def house_robber(houses,currentIndex):
            if currentIndex >= len(houses):
                return 0
            
            if currentIndex in index_list:
                return index_list[currentIndex]
            
            stealFirst = houses[currentIndex] + house_robber(houses,currentIndex + 2)
            skipFirst = house_robber(houses,currentIndex+1)
            
            if currentIndex not in index_list:
                index_list[currentIndex] = max(stealFirst,skipFirst)

           
            
            return max(stealFirst,skipFirst)

        index_list = {}
        print(house_robber(nums,0))
        










sol = Solution()
houses = [6,7,1,30,8,2,4]
sol.rob(houses)
