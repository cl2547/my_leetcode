class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        ans_list = nums[0:2]
        for i in range(2,len(nums),1):
            temp  = ans_list.copy()
            for j in range(len(temp)-1):
                temp[j] += nums[i]
            ans = max(temp)
            ans_list.append(ans)
        return ans_list[-1]