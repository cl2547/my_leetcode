# todo:optimize to run faster
import numpy as np
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        d = np.full((n, n), 2, np.int)
        rPalindrome = ""
        maxLength = 0
        start = 0
        end = 0
        # print(n)
        # special case:
        s2 = str(s[0]*n)

        if (s == s2):
            print("here")
            return s
        
        for i in range(n-1,-1,-1):
            for j in range(i,n,1):
                self.formPalindrome(s,d,i,j)
                if ((d[i,j] == 1) and ((j+1-i) > maxLength)):
                    maxLength = j+1-i
                    start = i
                    end = j

        rPalindrome = s[start:end+1]
        print(d)
        return rPalindrome
            
    def formPalindrome(self, s, d, i, j):
        if (d[i,j] == 2):
            if (i == j):
                d[i, j] = 1
            elif (i == j-1):
                d[i,j] = (s[i] == s[j])
            else:
                d[i,j] = (d[i+1,j-1] and (s[i] == s[j]))
            
        
        
    
            

