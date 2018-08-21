class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sList = []
        if (len(s)%2 != 0):
            return False
            
        for i in list(s):
            if (i == '(' or i== '{' or i == '['):
                sList.append(i)
            else:
                if (len(sList) == 0):
                    return False
                pop = sList[-1]
                if (self.isPair(pop, i) == False):
                    return False
                del sList[-1]
        if (sList == []):
            return True
        else:
            return False
    
    def isPair(self, s1, s2):
        if ((s1=='(' and s2==')') or (s1=='[' and s2==']') or (s1=='{' and s2=='}')):
            return True
        else:
            return False