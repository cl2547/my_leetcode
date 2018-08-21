class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums == None):
            return 0
        # temp = nums[0]
        pos = 0
        count = 0
        length = len(nums)
        while (count < length):
            if (pos == 0):
                temp = nums[0]
                pos += 1
                count += 1
            elif(nums[pos] == temp):
                del nums[pos]
                count += 1
            elif(nums[pos] != temp):
                temp = nums[pos]
                pos += 1
                count += 1
                    
        return len(nums)