class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 2:
            return [nums]
        
        result_list = []
        
        for i in range(len(nums)):
            temp_list = self.permute(nums[0:i] + nums[i+1:])
            for sub_list in temp_list:
                to_add = [nums[i]]+sub_list
                result_list.append(to_add)
        return result_list
        