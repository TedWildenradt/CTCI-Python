def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    dp = [0] * (len(nums)+1)
    dp[1] = nums[0]
    dp[2] = max(nums[:2])
    
    for i in range(3,len(nums)+1):
        dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
    return dp[i]

rob([2,7,9,3,1])