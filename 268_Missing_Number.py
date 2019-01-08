class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        total = maxNum*(maxNum+1)/2
        #if check missing value is max
        if total == sum(nums) and min(nums)==0:
            return maxNum+1
        elif total == sum(nums) and min(nums)!=0:
            return 0 
        #when missing value is not max number
        missingVal = total - sum(nums)
        return int(missingVal)