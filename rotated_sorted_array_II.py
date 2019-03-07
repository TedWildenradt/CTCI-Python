class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            midValue = nums[mid]
            if target == midValue:
                return True
            while start < mid and nums[start] == midValue:
                start += 1
            if nums[start] <= midValue:
                if nums[start] <= target < midValue:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if midValue < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

obj = Solution()
obj.search([1,3,1,1,1],3)