class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nums = list(str(x))
        pos = 0
        length = len(nums)
        for num in nums:
            if nums[pos] != nums[length-pos-1]:
                return False
            pos += 1
        return True