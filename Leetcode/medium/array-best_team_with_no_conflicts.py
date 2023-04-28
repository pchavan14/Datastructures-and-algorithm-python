class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """

 
        scores = [s for a,s in sorted(zip(ages, scores))]

        dp = scores[:]


        max_score = 0

        for curr in range(len(scores)):
            for prev in range(curr):
                if scores[prev] <= scores[curr]:
                    dp[curr] = max(dp[curr],dp[prev] + scores[curr])        
            max_score = max(max_score,dp[curr])
    
        print(dp)

        

        

        

        


      




sol = Solution()
scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
sol.bestTeamScore(scores,ages)
