class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsum = nums[0]
        maxsum = subsum
        for ele in nums[1:len(nums)]:
            if subsum < 0:
                subsum = 0
            subsum += ele
            if maxsum < subsum:
                maxsum = subsum
        return maxsum