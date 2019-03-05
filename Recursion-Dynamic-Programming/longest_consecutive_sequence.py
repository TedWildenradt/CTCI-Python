class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        
        output = 0
        
        for num in nums:
            count = 1
            if (num - 1) not in numSet:
                while num + 1 in numSet:
                    count += 1
                    num += 1
            output = max(output, count)
        return output

obj = Solution()
obj.longestConsecutive([100, 4, 200, 1, 3, 2])