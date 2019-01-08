class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n != 1:
            sum = 0
            for digit in str(n):
                sum += int(digit)**2
            n = sum
            if n in visited:
                return False
            else:
                visited.add(n)
        return True