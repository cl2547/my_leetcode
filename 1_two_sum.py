class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = 0
        length = len(nums)
        result = []
        for num in nums:
            pos2 = pos+1
            for subNum in nums[pos2:length+1]:
                if (num + subNum == target):
                    result = [pos, pos2]
                    break
                else:
                    pos2 += 1
            pos += 1
        return result
    