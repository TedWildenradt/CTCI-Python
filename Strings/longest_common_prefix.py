class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ''
        strs.sort(key=lambda x: len(x))
        i = 0
        
        while i < len(strs[0]):
          curr = strs[0][i]
          if all(map(lambda x: x[i] == curr, strs)):
            output += curr 
          else:
            break
          i += 1
        return output


obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])
# obj.longestCommonPrefix(["dog","racecar","car"])

x = min(["flower","flow","flight"],lambda x: len(x))