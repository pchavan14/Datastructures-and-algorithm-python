class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #top down
        def house_robber(houses,currentIndex,memo):
            if currentIndex >= len(houses):
                return 0
            elif currentIndex in memo:
                return memo[currentIndex]
            else:
                if currentIndex not in memo:
                    stealFirst = houses[currentIndex] + house_robber(houses , currentIndex + 2,memo)
                    skipFirst = house_robber(houses,currentIndex + 1,memo)
                    memo[currentIndex] = max(stealFirst,skipFirst)

            return memo[currentIndex] 
        
        def house_robber_bottom_up(houses):
            tb = [0] * (len(houses) + 2)
            
            for i in range(len(houses)-1,-1,-1):
               tb[i] = max(houses[i] + tb[i+2], tb[i+1])

            print(tb)

            return tb[0]



        memo = {}
        return house_robber_bottom_up(nums)

sol = Solution()
houses = [6,7,1,30,8,2,4]
print(sol.rob(houses))