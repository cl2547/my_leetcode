class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # create a dictionary to store the number looped
        nums = {0: 0}

        result = self.dfs(coins, amount, nums)
        if result == float("inf"):
            return -1
        return result

    def dfs(self, coins, target, nums):
        if target < 0:
            return float("inf")
        if target == 0:
            return 0
        if target in nums:
            return nums[target]
        nums[target] = float("inf")
        for c in coins:
            result = self.dfs(coins, target-c, nums)+1
            if nums[target] > result:
                nums[target] = result
        return nums[target]