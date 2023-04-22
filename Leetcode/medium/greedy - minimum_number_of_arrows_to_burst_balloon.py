class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        
        points = sorted(points,key=lambda x : x[1])

        arrows = 0
        i = 0
        j = 1
        while j < len(points):
            if points[i][1] >= points[j][0]:
                j += 1
            else:
                arrows += 1
                i = j
                j += 1
        arrows += 1

        return (arrows)
            







points = [[1,2],[2,3],[3,4],[4,5]]
sol = Solution()
sol.findMinArrowShots(points)
