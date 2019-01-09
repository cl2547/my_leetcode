class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        returnList = []
        stack = []
        for i in range(len(T)-1, -1, -1):
                #if the inserted value is large, remove all elements in stack that're smaller than that， return the diff between index of inserted value and the rightmost value
            while stack and T[i]>=T[stack[-1]]:
                stack.pop()
            
            if stack: #when stack is not empty
                returnList.insert(0,stack[-1]-i)
            else:
                returnList.insert(0,0)
            stack.append(i)
        return returnList
        