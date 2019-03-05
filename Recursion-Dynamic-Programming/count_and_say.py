class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 0:
            return ''
        if n == 1:
            return '1'
        newStr = ''
        prev = self.countAndSay(n - 1)
        
        i = 0
        while i < len(prev):
            count = 1
            while (i+1) < len(prev) and prev[i] == prev[i+1]:
                count += 1
                i += 1
            newStr += str(count) + prev[i]
            if i == len(prev) - 1:
                break
            i += 1
        return newStr

obj = Solution()
obj.countAndSay(6)