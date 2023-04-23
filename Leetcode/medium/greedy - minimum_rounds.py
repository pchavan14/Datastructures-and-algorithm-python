from collections import Counter
# class Solution(object):
#     def minimumRounds(self, tasks):
#         """
#         :type tasks: List[int]
#         :rtype: int
#         """


#         my_dict = Counter(tasks)

#         min_rounds = 0
        

#         for key, value in my_dict.items():
#             if value == 1:
#                 return -1
#             elif value == 2 or value == 3:
#                 min_rounds += 1
#             else:
#                 task_list = [3,2]
#                 while value:
#                     if value >= task_list[0]:
#                         value = value - task_list[0]
#                         min_rounds += 1
#                     else:
#                         task_list.pop(0)    
#                         if len(task_list) == 0 and value != 0:
#                             return -1    

#         return min_rounds

class Solution:
    def minimumRounds(self, tasks):
        frequency = Counter(tasks)
        res = 0
        for key,freq in frequency.items():
            if freq == 1:
                return -1
            elif (freq-2) % 3 == 0:
                print(key, freq)
                res += (freq-2) // 3 + 1
                print(res)
            elif (freq - 4) % 3 == 0:
                res += (freq - 4) // 3 +2
            elif freq % 3 == 0:
                res += freq // 3
            else:
                res += freq // 2
        return res
    
        


tasks = [2,2,3,3,4,4,4,4,4]
sol = Solution()
print(sol.minimumRounds(tasks))
