class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #naive approach: compare head and tail
        if head == None:
            return True
        temp = []
        shouldBreak = 0
        while True:
            if shouldBreak == 1:
                break
            temp.append(head.val)
            if head.next == None:
                shouldBreak = 1
            if head.next and shouldBreak == 0:
                head = head.next
        print(temp)
        left = 0
        right = len(temp)-1
        while left <= right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -=1
        return True