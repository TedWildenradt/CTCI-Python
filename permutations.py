class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
          return [[]]
        if len(nums) == 1:
          return [[nums[0]]]
        prev = self.permute(nums[:-1])
        new_perm = []
        for perm in prev:
          for i in range(len(perm) + 1):
            new_perm.append(perm[:i] + [nums[-1]] + perm[i:])
        return new_perm

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [num] + perm[i:])
            perms = new_perms
        return perms



obj = Solution()
obj.permute([1,2,3])