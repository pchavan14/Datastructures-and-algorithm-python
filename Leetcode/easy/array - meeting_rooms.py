intervals = [[0,30],[5,10],[15,20]]

def canAttenMeetings(intervals):
    if len(intervals) == 1:
        return True
    intervals.sort(key = lambda x : x[0])
    start = 0
    end = 0
    for element in intervals:
        if element[0] >= end:
            start = element[0]
            end = element[1]
        else:
            return False
    return True

            

print(canAttenMeetings([[7,10]]))