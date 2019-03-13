class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        self.flag = False
        
        def valid(s):
            if len(s) <= 1:
                return True
            if s[0] == s[-1]:
                return valid(s[1:-1])
            else:
                if self.flag:
                    return False
                else:
                    self.flag = True
                    # if s[0] == s[-2]:
                    #     return valid(s[:-1])
                    # elif s[1] == s[-1]:
                    #     return valid(s[1:])
                    # else:
                    #     return False
                    return valid(s[:-1]) or valid(s[1:])
                    
        return valid(s)

obj = Solution()
obj.validPalindrome("ebcbbececabbacecbbcbe")