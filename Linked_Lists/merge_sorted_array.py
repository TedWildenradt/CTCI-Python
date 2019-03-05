class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        k = n - 1
        last = m + n - 1
        
        while j >= 0 and k >= 0:
            if nums2[k] > nums1[j]:
                nums1[last], nums2[k] = nums2[k], nums1[last]
                k -= 1
            else:
                nums1[j], nums1[last] = nums1[last], nums1[j]
                j -= 1
            last -= 1
        if j < 0:
            nums1[:k+1] = nums2[:k+1]

obj = Solution()
nums1 = [1,2,3,4,0,0,0]
m = 4
nums2 = [2,5,6]
n = 3
obj.merge(nums1,m,nums2,n)