## sort activities based on some parameter



def activity_selection(activities):
    
    activities = sorted(activities,key= lambda x : x[2]) # O(nlogn)

    number_of_activities = 1
    i = 0
    j = 1

    while j < len(activities): # O(n)
        if activities[i][2] <= activities[j][1]:
            number_of_activities += 1
            i += 1
            j += 1
        else:
            j += 1

    print(number_of_activities)


activities = [["A1",0,6],
              ["A2",3,4],
              ["A3",1,2],
              ["A4",5,8],
              ["A5",5,7],
              ["A6",8,9]
            ]
activity_selection(activities)