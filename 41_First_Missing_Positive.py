class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #should have {1, 2, 3, ...} and put large/negative numbers on the rightmost
        i = 0
        while i<len(nums):
            val = nums[i]
            if nums[i] <= 0 or nums[i] > len(nums):
                i+=1
                continue
            if nums[i] == nums[val-1]:
                i+=1
                continue
            #swap the position
            nums[i], nums[val-1] = nums[val-1], nums[i]
        
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        