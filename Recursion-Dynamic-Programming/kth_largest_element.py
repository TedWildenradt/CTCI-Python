class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        length = len(nums)
        
        while True:
            idx = self.helper(nums,start,end)
            if idx == length - k:
                return nums[idx]
            elif idx < length - k:
                start = idx + 1
            else:
                end = idx
                
    def helper(self, nums,start,end):
        i = start
        for j in range(start,end):
            if nums[i] > nums[j]:
                nums[i+1],nums[j] = nums[j], nums[i+1]
                nums[i+1],nums[i] = nums[i], nums[i+1]
                i += 1
        return i

obj = Solution()
obj.findKthLargest([3,2,3,1,2,4,5,5,6],4)