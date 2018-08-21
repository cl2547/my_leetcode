class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestStr = ""
        pos = 0
        length = len(s)
        maxLen = 0
        for i in range(length):
            start = pos
            longestStr = ""
            while (start <= length-1):
                if (longestStr.find(s[start]) == -1):
                    longestStr += s[start]
                    start += 1
                else:
                    break
        
            if (len(longestStr) > maxLen):
                temp = longestStr[:]
                maxLen = len(temp)
            pos += 1
        
        return maxLen