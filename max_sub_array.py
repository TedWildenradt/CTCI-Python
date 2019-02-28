def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numsRev = nums[::-1]
    for i in range(1,len(nums)):
      nums[i] *= nums[i-1] or 1
      numsRev[i] *= numsRev[i-1] or 1
    return max(numsRev + nums)
      

maxProduct([2,3,-2,4,-7,-8,12])