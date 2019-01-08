class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1] and i%2==0:
                return nums[i]
        return nums[-1]