class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sample_str = []
        
        i = 0
        j = 0
        res = 0

        while j < len(s):
            if s[j] not in sample_str:
                sample_str.append(s[j])
                j = j + 1
                res = max(res,j-i)
                print(res)
            else:
                sample_str.remove(s[i])
                i = i + 1

       
       


            




s = "abcabcbb"
sol = Solution()
sol.lengthOfLongestSubstring(s)