class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
          return True
        dp = [False] * len(nums)
        dp[0] = True 

        for idx, num in enumerate(nums):
          if not dp[idx]:
            return False
          if num == 0:
            continue
          for i in range(num,-1,-1):
            if idx + i >= len(nums):
              continue
            if dp[idx+i]:
              break
            dp[idx + i] = True 
        
        return all(dp)

class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        highest_access = 0
        numlen = len(nums) 
        
        for i in range(numlen):
            if i + nums[i] > highest_access and i <= highest_access:
                highest_access = i + nums[i]
        
        return highest_access >= numlen - 1

obj = Solution2()
obj.canJump([2,0,0])
        
