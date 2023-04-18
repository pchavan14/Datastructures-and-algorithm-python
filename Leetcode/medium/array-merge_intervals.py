class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return None


        intervals = sorted(intervals,key=lambda x:x[0])

        #print(intervals)

        result = []
        result.append(intervals[0])
        

        for i in range(1,len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            elif result[-1][1] >= intervals[i][0] and result[-1][1] < intervals[i][1]:
                result[-1][1] = intervals[i][1]
            else:
                continue

        print (result)
            



intervals = [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
sol = Solution()
sol.merge(intervals)