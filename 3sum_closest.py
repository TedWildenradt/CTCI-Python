def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    closest = currDiff = float('inf')
    
    nums.sort()
    
    for i in range(len(nums)):
        
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            diff = abs(target - total)
            
            if diff < currDiff:
                closest = total
                currDiff = diff
            if total < target:
                j += 1
            elif total > target:
                k -= 1
            else:
                return closest
    return closest

threeSumClosest([-1, 2, 1, -4],1)