class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for word in wordDict:
            if word not in s:
                return False
            else:
                idx = wordDict.index(word)
                end = len(word)
                s = s[:idx] + s[(idx + end):]
        return True


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
obj = Solution()
obj.wordBreak(s,wordDict)