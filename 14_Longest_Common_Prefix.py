class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        minLen = len(strs[0])
        
        # find out the minimum number of loops to go through to find prefix
        for string in strs:
            if (minLen > len(string)):
                minLen = len(string)
        prefix = ""
        if (minLen == 0):
            return prefix
        for i in range(minLen):
            val = strs[0][i]
            for string in strs:
                if (val != string[i]): return prefix
            
            prefix += val
        return prefix