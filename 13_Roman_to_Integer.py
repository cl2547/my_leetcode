class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = list(str(s))
        #first find if there is a small roman letter before a large roman letter
        # if there exists, group them together,find the true value
        pos = 0
        sum = 0
        preNum = ""
        for num in nums:
            if (pos < len(nums)-1):
                val = self.getVal(num, nums[pos+1])
            else:
                val = self.getVal(num)
            pos += 1
            sum += val
        return sum
    
    def getVal(self, num, num2="I"):
        val = 0
        if (num == "I") and (num2 == "V" or num2 == "X"):
            val = -1
        elif (num == "X") and (num2 == "L" or num2 == "C"):
            val = -10
        elif (num == "C") and (num2 == "D" or num2 == "M"):
            val = -100
        elif (num == "I"):
            val = 1
        elif (num == "V"):
            val = 5
        elif (num == "X"):
            val = 10
        elif (num == "L"):
            val = 50
        elif (num == "C"):
            val = 100
        elif (num == "D"):
            val = 500
        elif (num == "M"):
            val = 1000
        return val