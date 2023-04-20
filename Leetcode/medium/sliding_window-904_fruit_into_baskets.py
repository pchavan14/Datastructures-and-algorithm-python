
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_length = 0
        sample_list = {}
        for i in range(len(fruits)):
            sample_list[fruits[i]] = 1
            for j in range(i,len(fruits)):
                if fruits[j] != fruits[i]:
                    if sum(sample_list.keys()) <= 2:
                        sample_list[fruits[j]] = 1
                    else:
                        max_length = max(sum(sample_list.keys()),max_length)
                        sample_list = {}
                        break
                else:
                    sample_list[fruits[i]] += 1
                    print(sample_list)

        print(max_length)
                    

        

        





fruits =[1,2]
sol = Solution()
sol.totalFruit(fruits)
