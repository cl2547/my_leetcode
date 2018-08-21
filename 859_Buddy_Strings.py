class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if (len(A) != len(B)):
            return False
        #for the same string A and B, if one char appears more than once, they are changable
        if (A == B):
            if (len(list(A)) != len(set(list(A)))):
                return True
            else:
                return False
            
        #count number of different letters b/t A and B, find pos of differences
        count = 0
        pos = []
        for i in range(len(A)):
            if (A[i] != B[i]):
                count += 1
                pos.append(i)
        if (count != 2):
            return False
        else:
            Acopy = (A + '.')[:-1]
            Alist = list(A)
            Acopylist = list(Acopy)
            Acopylist[pos[0]] = Alist[pos[1]]
            Acopylist[pos[1]] = Alist[pos[0]]
            Acopy = ''.join(Acopylist)
            print(Acopy)
            if (Acopy == B):
                return True
            else:
                return False