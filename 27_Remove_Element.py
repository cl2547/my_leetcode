class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        length = len(nums)
        for i in range(length):
            if (nums[pos] == val):
                del nums[pos]
            else:
                pos += 1
        
        return len(nums)