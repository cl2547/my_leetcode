class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        #when only climbing 1 stair
        for i in range(n):
            if (i == 0):
                result.append(1)
            elif (i == 1):
                result.append(2)
            else:
                result.append(result[i-1] + result[i-2])
        
        return result[-1]