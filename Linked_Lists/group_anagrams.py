from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for word in strs:
            key = tuple(sorted(list(word)))
            hash[key] = hash.get(key,[]) + [word] 
        return hash.values()

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
obj.groupAnagrams(arr)