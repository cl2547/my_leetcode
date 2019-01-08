class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_list = []
        for num in nums:
            if len(k_list)<k:
                k_list.append(num)
            else:
                min_val = min(k_list)
                if num > min_val:
                    k_list.remove(min(k_list))
                    k_list.append(num)
        return min(k_list)