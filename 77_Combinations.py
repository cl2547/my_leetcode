class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        interim = []
        if k < 0:
            return []
        for i in range(1,n+1):
            interim.append([i])
        if k == 1:
            return interim
        else:
            final_list = self.combine_helper(n, k, interim, 2)
        return final_list
    
    def combine_helper(self, n, k, interim, level):
        # when the interim already have lists with k-1 element
        temp_list = []
        for element in interim:
            if element[-1] < n:
                for i in range(element[-1]+1, n+1):
                    to_add = element.copy()
                    to_add.append(i)
                    temp_list.append(to_add)
        if level == k:
            return temp_list
        else:
            temp_list = self.combine_helper(n, k, temp_list, level+1)
            return temp_list