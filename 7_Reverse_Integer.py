class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums = list(str(x))
        result = ""
        startZero = 1
        for num in nums:
            if (num != "-"):
                if (int(num)!= 0):
                    result = num + result
                    startZero = 0
                elif (int(num)== 0 and startZero == 0):
                    result = num + result
        if (x < 0):
            result = "-" + result
        if (result == ""):
            result = "0"
        result = int(result)
        
        min = pow(-2,31)
        max = pow(2,31)-1
        if (result < min or result > max):
            return 0
        return result