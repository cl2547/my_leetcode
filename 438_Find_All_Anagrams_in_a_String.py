class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        temp = {} # record what values are needed
        target = {}
        
        #put p in target dict:
        for i in p:
            target[i] = 0
        for i in p:
            target[i] += 1
        
        def isAnagram(a,b,target):
            #initialize dict
            temp = {}
            for i in b:
                temp[i] = 0

            if sorted(a) == sorted(b):
                return temp
            else:
                temp = target.copy()
                for i in range(len(a)):
                    val = a[i]
                    if val in b:
                        temp[val] -= 1
            print(temp)
            return temp
        
        for i in range(len(s)-len(p)+1):
            if i == 0:
                temp = isAnagram(s[:len(p)], p, target)
            else:
                deleted = s[i-1]
                added = s[i+len(p)-1]
                if deleted in p:
                    temp[deleted] += 1
                if added in p:
                    temp[added] -= 1
            if all(value == 0 for value in temp.values()) == 1:
                ans.append(i)
        return ans