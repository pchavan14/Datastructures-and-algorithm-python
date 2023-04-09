#heapq algorithm - priority queue algorithm 
#Min heap - smallest element is always at the root

#optimal scheduling problem can make use of heapq(priority queue implementation using heap)

#brute force - whenever new meeting availability comes , check all the rooms 

#Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
#return the minimum number of conference rooms required.

#sort the intervals on start time 
import heapq
class Solution:
    def minMeetingRooms(self,intervals):
        
        #edge case
        if len(intervals) == 1:
            return 1
        elif len(intervals) == 0:
            return 0
        else:
            #sort the meeting on its start time
            intervals.sort(key = lambda x : x[0])

            #define a heap (meetings are removed according to the finish time)
            free_rooms = []
            
            #inserted the end time of the meeting started the earliest
            heapq.heappush(free_rooms,intervals[0][1])

            for i in intervals[1:]: #O(n)
                #the meeting has greter start time then the meeting with shortest end time , so it can use a free room
                if free_rooms[0] <= i[0]:
                    heapq.heappop(free_rooms) #O(LogN)
                #if not a new meeting room is allocated to it
                heapq.heappush(free_rooms,i[1]) #O(LogN)

            return len(free_rooms)
                
            

intervals = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
sol = Solution()
min_meeting_rooms = sol.minMeetingRooms(intervals)
print(min_meeting_rooms)

#Time complexity - O(NLogN)










    

