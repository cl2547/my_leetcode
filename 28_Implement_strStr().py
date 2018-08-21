class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle == ""):
            return 0
        
        length = len(haystack)
        length2 = len(needle)
        for i in range(length):
            if (haystack[i:i+length2] == needle):
                return i
        
        return -1