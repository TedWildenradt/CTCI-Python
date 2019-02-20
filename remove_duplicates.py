def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    i = 0
    
    length = 1
    
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            length += 1
    return length

removeDuplicates([0,0,1,1,1,2,2,3,3,4])