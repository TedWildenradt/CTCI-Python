class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        i = len(digits) - 1
        
        while i >= 0:
            digits[i] = digits[i] + 1
            if digits[i] > 9:
                digits[i] = 0
                carry = True
            else:
                carry = False
                break
            i -= 1
        if carry:
          return [1] + digits
        return digits

obj = Solution()
obj.plusOne([])