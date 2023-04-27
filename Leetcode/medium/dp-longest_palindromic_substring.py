class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        visited = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                input = s[i:j+1]
                if input not in visited and self.is_string_palindrome(input, visited):
                    result.append(input)
        result.sort(key=lambda x:len(x), reverse=True)
        return result[0]


    def is_string_palindrome(self, input, visited):
        i = 0
        j = len(input)-1

        while i<j:
            if input[i] != input[j]:
                return False
            i += 1
            j -= 1
        visited.add(input)
        return True





s = 'cbbd'
sol = Solution()
print(sol.longestPalindrome(s))