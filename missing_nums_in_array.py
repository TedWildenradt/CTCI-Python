def missing(nums):
    output = []
    
    for i in range(len(nums)):
        val = abs(nums[i])
        if nums[val - 1] > 0:
            nums[val - 1] = nums[val - 1] * -1
    for i in range(len(nums)):
        if nums[i] > 0:
            output.append(i + 1)
    return output

missing([4,3,2,7,8,2,3,1])
