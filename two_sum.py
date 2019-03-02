class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            hash[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in hash and i != hash[nums[i]]:
                return [i,hash[nums[i]]]

obj = Solution()
obj.twoSum([2, 7, 11, 15], 9)