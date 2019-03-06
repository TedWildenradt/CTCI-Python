class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        for i in range(len(s)):
            output += self.palindromeCounter(s,i,i)
            output += self.palindromeCounter(s,i,i+1)
        return output
    
    def palindromeCounter(self,string,left,right):
        counter = 0
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
            counter += 1
        return counter

obj = Solution()
obj.countSubstrings('aaa')