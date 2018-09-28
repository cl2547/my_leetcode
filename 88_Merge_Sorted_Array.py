class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0 #use i to track postion of nums1 and j to track position of nums2
        numInsert = 0
        totalLength = len(nums1)
        
        while j < n:
            added = False
            num2 = nums2[j]
            if (num2 <= nums1[i]):
                nums1.insert(i,num2)
                nums1.pop()
            else:
                #try add element before end of array
                while (i+1<=len(nums1)):
                    if (num2 <= nums1[i]):
                        nums1.insert(i,num2)
                        nums1.pop()
                        added = True
                        break
                    i += 1
                if (added == False):
                    #when reaching end of index
                    nums1.insert(j+m,num2)
                    i = j+m
                    nums1.pop()
            j += 1
        
        